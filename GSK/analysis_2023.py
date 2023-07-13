import pandas as pd
import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Sample dataset (assuming you have a DataFrame with 'survey_text' column)
data = pd.read_csv('customer_feedback.csv')

# Tokenize and encode the survey text using BERT tokenizer
tokenized_text = data['survey_text'].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

# Pad the tokenized sequences to a fixed length
max_length = max(map(len, tokenized_text))
padded_sequences = torch.tensor([seq + [0] * (max_length - len(seq)) for seq in tokenized_text])

# Forward pass through the BERT model
with torch.no_grad():
    outputs = model(padded_sequences)

# Extract the last hidden state of BERT (output embeddings)
last_hidden_state = outputs.last_hidden_state

# Aggregate the textual data
aggregated_data = last_hidden_state.mean(dim=1)  # Average the embeddings over the sequence length

# Summarize the textual data (using the first token, [CLS])
summaries = []
for i in range(len(data)):
    summary = tokenizer.decode(padded_sequences[i][0:2])  # Decoding the first two tokens
    summaries.append(summary)

# Enrich the textual data (perform additional analysis, e.g., sentiment analysis)
# You can use additional NLP libraries or models for this task

# Example: Printing the aggregated data, summaries, and enriched information
for i in range(len(data)):
    print(f"Survey {i+1}:")
    print("Aggregated Data:")
    print(aggregated_data[i])
    print("Summary:")
    print(summaries[i])
    print("Enriched Information:")
    # Print additional analysis results or enriched information
    print()
