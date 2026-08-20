import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6]
NP -> 'John' [0.4]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'dog' [1.0]
V -> 'saw' [1.0]
""")

sentence = input("Enter a sentence: ").split()

parser = ViterbiParser(grammar)

print("\nMost Probable Parse:")

try:
    for tree in parser.parse(sentence):
        print(tree)
        tree.pretty_print()
        break
except ValueError:
    print("No valid parse found.")