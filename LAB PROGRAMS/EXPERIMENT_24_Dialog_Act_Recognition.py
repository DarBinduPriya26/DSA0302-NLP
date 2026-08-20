import re

text = input("Enter a dialogue: ")

text_lower = text.lower()

if re.search(r'\b(hello|hi|hey)\b', text_lower):
    dialog_act = "Greeting"

elif re.search(r'\b(thank|thanks)\b', text_lower):
    dialog_act = "Thanking"

elif re.search(r'\b(bye|goodbye)\b', text_lower):
    dialog_act = "Goodbye"

elif re.search(r'\b(please|could you|can you)\b', text_lower):
    dialog_act = "Request"

elif "?" in text:
    dialog_act = "Question"

else:
    dialog_act = "Statement"

print("\nDialog Act:", dialog_act)