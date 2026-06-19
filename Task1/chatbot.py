responses = {
    "hello": "Hey there! How are you doing?",
    "hi": "Hi! What's up?",
    "how are you": "I'm just a bunch of if-else statements but I'm doing great!",
    "what is your name": "I'm a simple rule based chatbot, made for project 1.",
    "what can you do": "Right now I can only reply to a few fixed messages lol",
    "help": "Try saying hello, asking my name, or just type bye to leave.",
    "bye": "Goodbye! Have a nice day.",
    "exit": "Goodbye! Have a nice day.",
    "quit": "Goodbye! Have a nice day."
}

exit_words = ["bye", "exit", "quit"]

print("Chatbot: Hi, I'm your rule based assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    clean_input = user_input.lower().strip()

    if clean_input in exit_words:
        print("Chatbot:", responses[clean_input])
        break

    reply = responses.get(clean_input, "Sorry, I don't understand that yet.")
    print("Chatbot:", reply)
