import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport
import torch
from transformers import BertTokenizer, BertModel


# Syntax of read_table()
pd.read_table('case_study_data.tsv', sep=NoDefault.no_default, delimiter=None, header='infer', names=NoDefault.no_default, index_col=None, usecols=None, squeeze=None, prefix=NoDefault.no_default, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)


# Read TSV file into DataFrame
df = pd.read_table('case_study_data.tsv')
print(df)

# columns: uniqueID, drugName, review, date

# EDA: ydata-profiling
profile = ProfileReport(df, title="Case Study Data Profiling Report")

# Load pre-trained BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Sample dataset (assuming you have a DataFrame with 'survey_text' column)
data = pd.read_table('case_study_data.tsv')

# Tokenize and encode the survey text using BERT tokenizer
tokenized_text = data['review'].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

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
