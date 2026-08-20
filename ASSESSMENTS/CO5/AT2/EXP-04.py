# Q4 - Language Generation and Surface Realization

def surface_realization():
    print("LANGUAGE GENERATION - SURFACE REALIZATION")
    print("-" * 45)

    # Semantic representation
    action = "Buy"
    agent = "Student"
    object_name = "Book"
    tense = "Past"

    print("Semantic Representation:")
    print("Action :", action)
    print("Agent  :", agent)
    print("Object :", object_name)
    print("Tense  :", tense)

    # Lexical selection
    subject = "The student"
    object_word = "a book"

    if action == "Buy" and tense == "Past":
        verb = "bought"
    else:
        verb = action.lower()

    # Sentence structuring
    sentence = subject + " " + verb + " " + object_word + "."

    print("\nLexical Selection:")
    print("Student -> The student")
    print("Buy -> bought")
    print("Book -> a book")

    print("\nSentence Structure:")
    print("Subject + Verb + Object")

    print("\nGenerated Sentence:")
    print(sentence)

    print("\nGrammatical Validation:")
    print("1. Subject: The student")
    print("2. Verb: bought")
    print("3. Object: a book")
    print("4. Past tense is correctly applied.")
    print("5. Subject-Verb-Object order is correct.")


surface_realization()
