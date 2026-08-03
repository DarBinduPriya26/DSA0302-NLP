words = ["played", "player", "playing"]

print("-" * 80)
print("{:<12} {:<10} {:<18} {:<15} {:<12}".format(
    "Word", "Stem", "Removed Affix", "Type", "Normalized"))
print("-" * 80)

for word in words:

    if word.endswith("ed"):
        stem = "play"
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = "play"
        affix = "er"
        t = "Derivational"

    elif word.endswith("ing"):
        stem = "play"
        affix = "ing"
        t = "Inflectional"

    print("{:<12} {:<10} {:<18} {:<15} {:<12}".format(
        word, stem, affix, t, stem))
