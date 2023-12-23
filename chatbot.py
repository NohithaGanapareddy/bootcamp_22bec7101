def chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ").lower()

        # Check if the user wants to exit
        if user_input == 'exit':
            print("Goodbye! Have a great day.")
            break

        # Simple conditional responses
        elif 'hello' in user_input:
            print("Chatbot: Hi there!")

        elif 'how are you' in user_input:
            print("Chatbot: I'm just a computer program, but thanks for asking!")

        elif 'your name' in user_input:
            print("Chatbot: I'm a chatbot. You can call me ChatBot3000!")

        elif 'age' in user_input:
            print("Chatbot: I don't have an age. I'm always up-to-date!")

        else:
            print("Chatbot: I'm not sure how to respond to that. Ask me something else.")

if _name_ == "_main_":
    chatbot()