# Simple AI Chatbot

def chatbot():
    print("Chatbot: Hello! I am your AI chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I am just a program, but I am doing great!")

        elif "your name" in user_input:
            print("Chatbot: I am a simple AI chatbot created using Python.")

        elif "help" in user_input:
            print("Chatbot: I can answer basic questions. Try asking something!")

        else:
            print("Chatbot: Sorry, I don't understand that yet.")

# Run chatbot
chatbot()