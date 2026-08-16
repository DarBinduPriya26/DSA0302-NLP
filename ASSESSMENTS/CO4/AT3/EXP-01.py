import nltk
import spacy

# -------------------------------
# Context-Free Grammar (CFG)
# -------------------------------
grammar = """
S -> NP VP
NP -> Det N
NP -> N
VP -> V NP
Det -> 'The'
N -> 'doctor' | 'medicine'
V -> 'prescribed'
"""

# Create CFG
cfg = nltk.CFG.fromstring(grammar)

# Create Chart Parser
parser = nltk.ChartParser(cfg)

# Input sentence
sentence = "The doctor prescribed medicine".split()

print("Sentence:")
print(" ".join(sentence))

# -------------------------------
# CFG Parsing
# -------------------------------
print("\nCFG Tree:")

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No parse tree found.")

# -------------------------------
# spaCy Dependency Parsing
# -------------------------------
print("\nDependency Relations:")

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("spaCy English model is not installed.")
    print("Run: python -m spacy download en_core_web_sm")
else:
    doc = nlp("The doctor prescribed medicine")

    for token in doc:
        print(token.text, "->", token.dep_, "->", token.head.text)
