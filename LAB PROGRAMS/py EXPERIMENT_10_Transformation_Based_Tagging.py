# Transformation-Based POS Tagging

# Input sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

# Step 1: Assign default tag NN to all words
tags = []

for word in words:
    tags.append([word, "NN"])

# Step 2: Apply transformation rules
for item in tags:
    word = item[0].lower()

    if word in ["the", "a", "an"]:
        item[1] = "DT"

    elif word in ["is", "am", "are", "was", "were"]:
        item[1] = "VB"

    elif word.endswith("ing"):
        item[1] = "VBG"

    elif word.endswith("ly"):
        item[1] = "RB"

    elif word.endswith("ed"):
        item[1] = "VBD"

# Display output
print("\nWord\t\tPOS Tag")
print("-" * 30)

for word, tag in tags:
    print(f"{word}\t\t{tag}")