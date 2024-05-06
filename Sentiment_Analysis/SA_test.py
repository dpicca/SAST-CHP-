from gpt4all import GPT4All
from transformers import AutoTokenizer, AutoModelForCausalLM
model_path = 'lzw1008/Emollama-chat-13b'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map='auto')
# model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
output = model.generate("The capital of France is ", max_tokens=10)
print(output)