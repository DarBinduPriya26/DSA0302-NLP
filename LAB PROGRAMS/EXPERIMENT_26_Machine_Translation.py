from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Loading translation model...")

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = input("Enter English text: ")

inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

translation = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nEnglish:")
print(text)

print("\nFrench:")
print(translation)