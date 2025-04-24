import torch
from zlib_ng import zlib_ng

def perplexity(model, tokenizer, input):
    tokenized_input = tokenizer(input, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = model(**tokenized_input, labels=tokenized_input["input_ids"])
        loss = outputs.loss
        perplexity = torch.exp(loss)
    return perplexity.item()

def zlib_entropy(input):
    text_bytes = input.encode('utf-8')
    compressed_data = zlib_ng.compress(text_bytes)
    entropy_bits = len(compressed_data)
    return entropy_bits

def zlib_perplexity_ratio(model, tokenizer, input):
    perplexity_value = perplexity(model, tokenizer, input)
    entropy_value = zlib_entropy(input)
    return entropy_value, perplexity_value