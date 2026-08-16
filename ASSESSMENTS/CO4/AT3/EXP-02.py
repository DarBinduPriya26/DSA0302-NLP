import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

# Define the Context-Free Grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
VP -> V
Det -> 'The'
N -> 'student'
V -> 'wants'
""")

# Create Earley Chart Parser
parser = EarleyChartParser(grammar)

# Input sentence
sentence = "The student wants".split()

# Perform parsing
print("Sentence:")
print(" ".join(sentence))

print("\nEarley Parsing Result:")

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
else:
    print("No valid parse tree found.")
