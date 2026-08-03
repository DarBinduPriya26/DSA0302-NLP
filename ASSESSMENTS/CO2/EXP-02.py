words = ["unhappy", "happiness", "happily"]

print("-" * 85)
print("{:<15} {:<10} {:<12} {:<10} {:<15} {:<12}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("-" * 85)

for word in words:

    if word == "unhappy":
        prefix = "un"
        root = "happy"
        suffix = "-"
        t = "Derivational"

    elif word == "happiness":
        prefix = "-"
        root = "happy"
        suffix = "ness"
        t = "Derivational"

    elif word == "happily":
        prefix = "-"
        root = "happy"
        suffix = "ly"
        t = "Derivational"

    print("{:<15} {:<10} {:<12} {:<10} {:<15} {:<12}".format(
        word, prefix, root, suffix, t, root))
