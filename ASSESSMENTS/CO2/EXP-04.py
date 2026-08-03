words = ["writes", "writing", "written"]

print("-" * 95)
print("{:<12} {:<25} {:<12} {:<12} {:<12}".format(
    "Word", "Transition Path", "Pattern", "Root", "Normalized"))
print("-" * 95)

for word in words:

    if word == "writes":
        path = "q0 -> q1 -> q2"
        pattern = "Regular"
        root = "write"

    elif word == "writing":
        path = "q0 -> q1 -> q3"
        pattern = "Regular"
        root = "write"

    elif word == "written":
        path = "q0 -> q4 -> q5"
        pattern = "Irregular"
        root = "write"

    print("{:<12} {:<25} {:<12} {:<12} {:<12}".format(
        word, path, pattern, root, root))
