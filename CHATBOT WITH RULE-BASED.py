def chatbot():
    print("Chatbot: Hi! I'm your assistant. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        
        if "bye" in user_input:
            print("Chatbot: Bye! Have a great day 😊")
            break
        
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How are you doing?")

        elif "i am good" in user_input or "i'm doing great!" in user_input:
            print("Chatbot: Glad to hear it! ")    
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! What about you?")
        
        elif "what's your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot!")
        
        elif "time" in user_input:
            import datetime
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}")

        else:
            print("Chatbot: I'm not sure I understand. Can you rephrase?")
chatbot()
