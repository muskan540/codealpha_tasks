import nltk
from nltk.chat.util import Chat, reflections

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I assist you today?", "Hi there! How are you?"]
    ],
    [
        r"what is your name\?",
        ["I'm a chatbot created to help you. You can call me ChatBot."]
    ],
    [
        r"how are you\?",
        ["I'm just a program, but I'm functioning as expected! How about you?"]
    ],
    [
        r"tell me about (.*)",
        ["Sure, what would you like to know about %1?", "Can you specify more about %1?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later! Take care."]
    ]
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("ChatBot: Hi! I'm your assistant. Type 'quit' to end the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["quit", "exit"]:
            print("ChatBot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print(f"ChatBot: {response}")
            else:
                print("ChatBot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    start_chat()