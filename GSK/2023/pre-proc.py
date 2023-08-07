# Install required libraries
# !pip install pandas nltk textblob

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import matplotlib.pyplot as plt

# Sample patient review dataset
df = pd.read_csv('ra.csv')

# Tokenization and Text Normalization
def preprocess_text(text):
    # Tokenization
    words = word_tokenize(text)
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(words)

# Applying Text Preprocessing to Reviews column
df['Cleaned_Reviews'] = df['Reviews'].apply(preprocess_text)

# Sentiment Analysis
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Applying Sentiment Analysis to Cleaned_Reviews column
df['Sentiment'] = df['Cleaned_Reviews'].apply(perform_sentiment_analysis)

# Data Visualization
# Bar chart for sentiment distribution
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Analysis Results')
plt.show()

# Bar chart for top 10 most common conditions
top_conditions = df['Condition'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
plt.bar(top_conditions.index, top_conditions.values)
plt.xlabel('Condition')
plt.ylabel('Count')
plt.title('Top 10 Most Common Conditions')
plt.xticks(rotation=45, ha='right')
plt.show()

# Word cloud for drug mentions in reviews
from wordcloud import WordCloud
drug_mentions = ' '.join(df['Drug'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(drug_mentions)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Drug Mentions in Reviews')
plt.show()

# Display the modified DataFrame with sentiment analysis results
print(df[['Condition', 'Drug', 'Reviews', 'Sentiment']])
