import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Download required resources
nltk.download("punkt")
nltk.download("punkt_tab")

# Define rule-based patterns
patterns = [
    (r'.*ing$', 'VBG'),      # Words ending with ing
    (r'.*ed$', 'VBD'),       # Words ending with ed
    (r'.*ly$', 'RB'),        # Adverbs
    (r'.*es$', 'VBZ'),       # Verbs ending with es
    (r'.*s$', 'NNS'),        # Plural nouns
    (r'.*able$', 'JJ'),      # Adjectives
    (r'.*ness$', 'NN'),      # Nouns
    (r'.*ment$', 'NN'),      # Nouns
    (r'^[Tt]he$', 'DT'),     # Determiner
    (r'^[Aa]$', 'DT'),       # Determiner
    (r'^[Aa]n$', 'DT'),      # Determiner
    (r'.*', 'NN')            # Default tag
]

# Create the RegexpTagger
tagger = RegexpTagger(patterns)

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize sentence
words = word_tokenize(sentence)

# Tag words
result = tagger.tag(words)

print("\nWord\t\tPOS Tag")
print("-" * 30)

for word, tag in result:
    print(f"{word}\t\t{tag}")