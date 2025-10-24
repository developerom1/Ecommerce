import sys
import os
sys.path.append("utils")

from speech import listen, speak
from nlp import get_bot_reply
from ecommerce import search_products

import openai

openai.api_key = "YOUR_OPENAI_API_KEY" # <-- Replace with your actual key

def main():
    print("Ecommerce Voicebot Agent Started.\n")
    history = []
    while True:
        user_input = listen()
        if not user_input:
            continue
        history.append({"role": "user", "content": user_input})
        reply = get_bot_reply(user_input, history)
        print(f"Bot: {reply}\n")
        speak(reply)
        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
