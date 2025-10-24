def search_products(query):
    products = [
        {"name": "Wireless Headphones", "price": "1499", "stock": 10},
        {"name": "Bluetooth Mouse", "price": "799", "stock": 20},
        {"name": "Smartwatch", "price": "4299", "stock": 5},
        {"name": "Android TV", "price": "23999", "stock": 2},
    ]
    results = [p for p in products if query.lower() in p['name'].lower()]
    return results
