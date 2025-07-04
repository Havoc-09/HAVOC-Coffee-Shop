☕ HAVOC Coffee Shop Project

A fully functional Python-based Coffee Shop Ordering System with a graphical user interface (GUI), PDF receipt generation, admin sales dashboard, and WhatsApp/Email order confirmations.

This project is developed to simulate a modern digital coffee shop experience — designed to help users place orders with ease while providing the admin with powerful sales insights.

---

## 🚀 Features

- 🖥️ **GUI-based Interface** using `tkinter`
- 🧾 **PDF Receipt Generator** with order details
- 📊 **Admin Dashboard** showing total sales and order breakdown
- 📱 **WhatsApp Order Confirmation** (auto-send to customer)
- 📧 Optional **Email Notification Support**
- 🧠 Smart order handling with item codes and price mapping
- 🔢 Supports dynamic menu customization
- 🐍 Fully written in Python

🛠️ Technologies Used

- Python 3
- tkinter (GUI)
- fpdf (PDF generation)
- pywhatkit (WhatsApp automation)
- datetime, os, and other Python modules

🧾 Sample Receipt

Receipt for Order
Item: Cappuccino
Quantity: 2
Total: ₹300
Date: 04/07/2025
Time: 5:32 PM
Thank you for visiting Havoc!

📂 Folder Structure

havoc-coffee-shop/
├── assets/
│ └── logo.png
├── receipts/
│ └── <order>.pdf
├── main.py
├── gui.py
├── dashboard.py
├── whatsapp.py
├── receipt_generator.py
├── .gitignore
├── README.md
└── requirements.txt
