import openai
from ecommerce import search_products

def get_bot_reply(user_input, history=[]):
    # Simple intent: product search
    if "find" in user_input or "search" in user_input:
        keyword = user_input.split("find")[-1].strip() or user_input.split("search")[-1].strip()
        products = search_products(keyword)
        if products:
            details = "; ".join([f"{p['name']} (Rs.{p['price']}, Stock: {p['stock']})" for p in products])
            return f"Found: {details}"
        else:
            return "No products found."
    # Otherwise, use GPT model
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history + [{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']
