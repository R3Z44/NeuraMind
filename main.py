# main.py

from modules.chatbot import ChatBot

def main():
    print("🤖 NeuraMind v1.0.0 – Transformer Chatbot")
    print("Type 'exit' to quit.\n")

    bot = ChatBot()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        response = bot.generate_response(user_input)
        print("NeuraMind:", response)

if __name__ == "__main__":
    main()
