# Experiment 25: Text Generation Demonstration

def generate_text(prompt):
    responses = {
        "artificial intelligence":
            "Artificial intelligence enables computers to perform tasks that normally require human intelligence.",

        "machine learning":
            "Machine learning allows computers to learn patterns from data and make predictions.",

        "natural language processing":
            "Natural language processing enables computers to understand and process human language."
    }

    prompt_lower = prompt.lower()

    for keyword, response in responses.items():
        if keyword in prompt_lower:
            return response

    return "Artificial intelligence is an important technology used in many real-world applications."


prompt = input("Enter your prompt: ")

generated_text = generate_text(prompt)

print("\nGenerated Text:")
print(generated_text)