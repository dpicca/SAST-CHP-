from gpt4all import GPT4All
from transformers import AutoTokenizer, AutoModelForCausalLM
model_path = 'myclassunil/Emollama-chat-13b-v0.1.gguf'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map='auto')
prompt = '''Human: 
Task: Assign a numerical value between 0 (least E) and 1 (most E) to represent the intensity of emotion E expressed in the text.
Text: @CScheiwiller can't stop smiling 😆😆😆
Emotion: joy
Intensity Score:'''
output = model.generate(prompt, max_tokens=10)
print(output)