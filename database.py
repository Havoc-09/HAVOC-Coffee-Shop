
import sqlite3
from datetime import datetime
import uuid

conn = sqlite3.connect("data/orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id TEXT PRIMARY KEY,
    items TEXT,
    total INTEGER,
    date TEXT
)
""")
conn.commit()

def save_order(order_dict, total_amount):
    order_id = str(uuid.uuid4())[:8]
    items = ", ".join([f"{item} x{qty}" for item, qty in order_dict.items()])
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO orders (id, items, total, date) VALUES (?, ?, ?, ?)",
                   (order_id, items, total_amount, date))
    conn.commit()
    return order_id
