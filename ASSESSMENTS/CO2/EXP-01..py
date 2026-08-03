words = ["connected", "connecting", "connection"]

print("-" * 75)
print("{:<15} {:<12} {:<10} {:<15} {:<12}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 75)

for word in words:

    if word.endswith("ed"):
        root = "connect"
        suffix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        root = "connect"
        suffix = "ing"
        t = "Inflectional"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        t = "Derivational"

    print("{:<15} {:<12} {:<10} {:<15} {:<12}".format(
        word, root, suffix, t, root))
