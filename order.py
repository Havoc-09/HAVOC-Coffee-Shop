
from menu import coffee_menu

def take_order():
    order = {}
    while True:
        code = input("Enter code or '--done': ").strip()
        if code == "--done":
            break
        if code in coffee_menu:
            qty = int(input(f"Qty of {coffee_menu[code]['name']}: "))
            order[code] = order.get(code, 0) + qty
    return order

def calculate_total(order):
    return sum(coffee_menu[code]['price'] * qty for code, qty in order.items())
