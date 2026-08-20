# Q3 - Dialogue Act Classification

def classify_dialogue():
    print("CONVERSATIONAL AGENT - DIALOGUE ACT CLASSIFICATION")
    print("-" * 55)

    conversation = [
        ("User", "Can you book a train ticket for me?", "Request"),
        ("Agent", "Sure, where would you like to travel?", "Question"),
        ("User", "I want to go to Chennai.", "Inform"),
        ("Agent", "Your ticket has been booked.", "Action / Confirmation")
    ]

    print("Conversation:\n")

    for speaker, utterance, act in conversation:
        print(speaker + ": " + utterance)
        print("Dialogue Act:", act)
        print()

    print("Dialogue Act Sequence:")
    print("REQUEST -> QUESTION -> INFORM -> ACTION / CONFIRMATION")

    print("\nEvaluation:")
    print("1. Request identifies the user's booking intention.")
    print("2. Question identifies the information required by the agent.")
    print("3. Inform provides the destination.")
    print("4. Action performs the requested booking.")
    print("5. Confirmation communicates successful completion.")

    print("\nConclusion:")
    print("Dialogue acts help the conversational agent understand")
    print("user intentions and maintain the correct conversation flow.")


classify_dialogue()
