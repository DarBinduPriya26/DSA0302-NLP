import nltk
from nltk import word_tokenize, pos_tag

# Download required resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(sentence)

# POS tagging
tags = pos_tag(words)

print("\nWord\t\tPOS Tag")
print("-" * 25)

for word, tag in tags:
    print(f"{word}\t\t{tag}")