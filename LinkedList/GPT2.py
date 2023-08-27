import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Sample input text
prompt = "once upon a time there was a beautiful princess who"

# Encode input text
input_ids = tokenizer.encode(prompt, return_tensors='pt')

# Generate text using the model
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode and print generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated text:", generated_text)
