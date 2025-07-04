
import sqlite3

def authenticate():
    return input("Enter admin password: ") == "havoc123"

def show_dashboard():
    conn = sqlite3.connect("data/orders.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), SUM(total) FROM orders")
    count, total = cur.fetchone()
    print(f"Total Orders: {count}, Revenue: ₹{total}")
    conn.close()
