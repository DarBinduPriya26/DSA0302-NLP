import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'student' | 'book'
V -> 'reads' | 'likes'
""")

sentence = input("Enter a sentence: ").lower().split()

parser = ChartParser(grammar)

print("\nNoun Phrases:")

found = False

for tree in parser.parse(sentence):

    for subtree in tree.subtrees():

        if subtree.label() == "NP":
            print("NP:", " ".join(subtree.leaves()))
            found = True

    if found:
        break

if not found:
    print("No noun phrases found.")