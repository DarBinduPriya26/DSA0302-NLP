# Q1 - Reference Resolution

def reference_resolution():
    print("REFERENCE RESOLUTION")
    print("-" * 40)

    text = "Ravi met Arun at the library. He borrowed a book and later returned it."

    print("Original Discourse:")
    print(text)

    # Entities identified from the discourse
    entities = ["Ravi", "Arun", "library", "book"]

    print("\nIdentified Entities:")
    for entity in entities:
        print("-", entity)

    # Pronoun resolution using discourse context
    he_antecedent = "Ravi"
    it_antecedent = "book"

    print("\nPronoun Resolution:")
    print("He ->", he_antecedent)
    print("it ->", it_antecedent)

    # Replace pronouns
    resolved_text = (
        "Ravi met Arun at the library. "
        "Ravi borrowed a book and later returned the book."
    )

    print("\nResolved Discourse:")
    print(resolved_text)

    print("\nValidation:")
    print("1. 'He' refers to Ravi because Ravi is the main discourse subject.")
    print("2. 'He' agrees with Ravi in gender and number.")
    print("3. 'it' refers to book because a book can be borrowed and returned.")
    print("4. The resolution is semantically and contextually consistent.")


reference_resolution()
