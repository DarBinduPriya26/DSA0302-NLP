import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

sentence = input("Enter a sentence: ").lower().split()

parser = RecursiveDescentParser(grammar)

print("\nParse Trees:")

found = False

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    found = True

if not found:
    print("No valid parse found.")