
from fpdf import FPDF
from datetime import datetime
import os

def generate_receipt(order_id, order_items, total_amount):
    os.makedirs("data/receipts", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"HAVOC Coffee Shop - Order ID: {order_id}", ln=True)
    pdf.cell(200, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    for code, item in order_items.items():
        pdf.cell(200, 10, f"{item['name']} x{item['qty']} - Rs.{item['price'] * item['qty']}", ln=True)
    pdf.cell(200, 10, f"Total: Rs.{total_amount}", ln=True)
    pdf.output(f"data/receipts/receipt_{order_id}.pdf")
