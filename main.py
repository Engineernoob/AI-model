import requests

def query_huggingface_model(prompt):
    API_URL = "https://api-inference.huggingface.co/models/cognitivecomputations/WizardLM-13B-Uncensored"
    headers = {"Authorization": "Bearer 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"}  # Replace with your actual API token
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()

def load_history():
    # ... (Your existing code to load conversation history) ...
    pass

def save_history(history):
    # ... (Your existing code to save conversation history) ...
    pass

def main():
    print("Loading conversational model...")

    past_conversation = load_history()
    conversation = past_conversation  # Adjust this based on how you want to use the history

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            save_history(conversation)
            break

        full_prompt = "\n".join(conversation + [user_input])  # Combine history with new input
        response = query_huggingface_model(full_prompt)
        
        # Extract and print the response (adjust based on the API's response format)
        ai_response = response.get("generated_text", "")
        print("AI:", ai_response)

        # Update conversation history
        conversation.append("You: " + user_input)
        conversation.append("AI: " + ai_response)

if __name__ == "__main__":
    main()
