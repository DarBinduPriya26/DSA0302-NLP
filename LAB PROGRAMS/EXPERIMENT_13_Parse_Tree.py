import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl' | 'ball'
V -> 'kicked' | 'saw'
""")

sentence = input("Enter a sentence: ").lower().split()

parser = ChartParser(grammar)

print("\nParse Tree:")

found = False

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    found = True
    break

if not found:
    print("No parse tree found.")