
coffee_menu = {
    "--init":   {"name": "Espresso", "price": 100},
    "--push":   {"name": "Cappuccino", "price": 150},
    "--merge":  {"name": "Latte", "price": 180},
    "--commit": {"name": "Mocha", "price": 200},
    "--cold":   {"name": "Cold Coffee", "price": 170}
}

def display_menu():
    for code, item in coffee_menu.items():
        print(f"{code}: {item['name']} - ₹{item['price']}")
