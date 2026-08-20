import nltk
from nltk.corpus import wordnet

nltk.download("wordnet")
nltk.download("omw-1.4")

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

if synsets:
    print("\nSynsets:")

    for synset in synsets[:5]:
        print("\nName:", synset.name())
        print("Definition:", synset.definition())
        print("Examples:", synset.examples())
else:
    print("No synsets found.")