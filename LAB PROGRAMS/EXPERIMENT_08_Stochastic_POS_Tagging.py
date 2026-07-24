import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import UnigramTagger

# Download required resources
nltk.download("punkt")
nltk.download("punkt_tab")

# Training data
train_data = [
    [("The", "DT"), ("boy", "NN"), ("plays", "VBZ"), ("cricket", "NN")],
    [("She", "PRP"), ("reads", "VBZ"), ("books", "NNS")],
    [("I", "PRP"), ("like", "VBP"), ("Python", "NNP")],
    [("They", "PRP"), ("are", "VBP"), ("students", "NNS")]
]

# Train the stochastic (probabilistic) tagger
tagger = UnigramTagger(train_data)

# Input
sentence = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(sentence)

# Tag the words
result = tagger.tag(words)

print("\nWord\t\tPOS Tag")
print("-" * 30)

for word, tag in result:
    print(f"{word}\t\t{tag}")