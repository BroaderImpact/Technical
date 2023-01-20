from transformers import DistilBertTokenizer, DistilBertForMaskedLM
import datasets

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-cased")
model = DistilBertForMaskedLM.from_pretrained("distilbert-base-cased")

dataset = datasets.load_dataset("wikitext", "wikitext-2-raw-v1")
train_dataset = dataset["train"]

# Take the 11th example
example = train_dataset[10]

# Tokenize the example
tokens = tokenizer.tokenize(example["text"])

# Mask the 6th token
tokens[5] = "[MASK]"

# Convert the tokens to their IDs
input_ids = tokenizer.convert_tokens_to_ids(tokens)

# Unmask the 6th token
outputs = model(input_ids)[0]
predicted_token = tokenizer.decode(torch.argmax(outputs[0, 5]).item())

print("The most probable predicted token is:", predicted_token)
