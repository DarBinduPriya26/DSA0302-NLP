import nltk
from nltk.corpus import wordnet

# Download WordNet (only the first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

word = input("Enter a word: ")

root = wordnet.morphy(word)

print("\nOriginal Word :", word)

if root:
    print("Root Word     :", root)
else:
    print("Root Word     : No root form found")