# !pip install -r requirements.txt

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Sample patient review dataset
data = {
    'Age': ['30-40', '50-60', '40-50'],
    'Condition': ['RA', 'COPD', 'SLE'],
    'Date': ['2022-08-01', '2022-08-02', '2022-08-03'],
    'Drug': ['DrugA', 'DrugB', 'DrugC'],
    'DrugId': [101, 102, 103],
    'EaseofUse': [4.5, 3.8, 4.0],
    'Effectiveness': [4.2, 3.9, 4.1],
    'Reviews': [
        'This drug has been a game-changer for my RA pain! Highly recommend!',
        'The side effects of DrugB were too severe. Not satisfied with its effectiveness.',
        'DrugC has significantly improved my SLE symptoms. Very satisfied.'
    ],
    'Satisfaction': [5, 2, 5],
    'Sex': ['Male', 'Female', 'Male'],
    'SideEffects': [
        'Nausea, headache', 'Dizziness, dry mouth, insomnia', 'Mild fatigue'
    ]
}

df = pd.DataFrame(data)

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