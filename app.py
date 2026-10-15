import ollama

messages = []

def chat():
    print("Chatbot IA Local com Memória")
  
    while True:
        user_input = input("Você: ")

        if user_input == "sair":
            break

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model= "gemma:2b",
            messages = messages
        )

        reply = response["message"]["content"]

        messages.append({"role": "assistant", "content": reply})

        print("Bot: ", reply)
        print()

if __name__ == "__main__":
    chat()