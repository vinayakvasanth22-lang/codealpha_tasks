def get_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye!"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple chatbot!"
    elif user_input in ["help", "what can you do"]:
        return "I can respond to: hello, how are you, bye, and more!"
    else:
        return "Sorry, I don't understand that. Try saying 'hello' or 'how are you'!"

def main():
    print("Chatbot is running! Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ")
        
        if not user_input.strip():
            continue
        
        response = get_response(user_input)
        print(f"Bot: {response}\n")
        
        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break

main()