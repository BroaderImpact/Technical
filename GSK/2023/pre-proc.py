# !pip install -r requirements.txt

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

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

print(df[['Condition', 'Drug', 'Reviews', 'Sentiment']])
