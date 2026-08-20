import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("punkt_tab")

sentence = input("Enter a sentence: ")
word = input("Enter the ambiguous word: ")

tokens = word_tokenize(sentence)

sense = lesk(tokens, word)

if sense:
    print("\nSelected Sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found.")