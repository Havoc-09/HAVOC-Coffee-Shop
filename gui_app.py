import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import pygame  # For music/sound
from menu import coffee_menu
from order import calculate_total
from database import save_order
from receipt import generate_receipt
from notifier import send_whatsapp_message

class HavocApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HAVOC Coffee Shop")
        self.root.geometry("500x600")
        self.root.configure(bg="#222")
        self.order = {}
        self.customer_name = ""
        self.customer_phone = ""

        # Initialize sound
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("bg.wav")
            pygame.mixer.music.play(-1)  # Loop forever
        except pygame.error:
            print("⚠️ Background music not found.")

        # Home Screen
        self.home_frame = tk.Frame(root, bg="#222")
        self.home_frame.pack(fill="both", expand=True)

        # Animated GIF
        self.canvas = tk.Canvas(self.home_frame, width=300, height=200, bg="#222", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open("welcome.gif"))]
        self.image_on_canvas = self.canvas.create_image(150, 100, image=self.sequence[0])
        self.animate_gif(0)

        greeting = tk.Label(self.home_frame, text="Helloww Pal...!!", font=("Helvetica", 20, "bold"), fg="white", bg="#222")
        greeting.pack(pady=5)

        self.name_entry = tk.Entry(self.home_frame, font=("Helvetica", 14))
        self.name_entry.pack(pady=10)
        self.name_entry.insert(0, "What's your name, pal?")

        self.phone_entry = tk.Entry(self.home_frame, font=("Helvetica", 14))
        self.phone_entry.pack(pady=5)
        self.phone_entry.insert(0, "Enter your phone (+91...)")

        next_button = tk.Button(self.home_frame, text="NEXT →", font=("Helvetica", 16), bg="#28a745", fg="white", command=self.show_main_page)
        next_button.pack(pady=10)

        # Main Screen Frame
        self.main_frame = tk.Frame(root, bg="#222")

        self.title_label = tk.Label(self.main_frame, text="", font=("Helvetica", 18, "bold"), fg="white", bg="#222")
        self.title_label.pack(pady=10)

        self.items_frame = tk.Frame(self.main_frame, bg="#222")
        self.items_frame.pack(pady=10)

        for code, item in coffee_menu.items():
            self.create_item(code, item)

        self.total_label = tk.Label(self.main_frame, text="Total: ₹0", font=("Helvetica", 14), fg="white", bg="#222")
        self.total_label.pack(pady=10)

        self.place_order_btn = tk.Button(self.main_frame, text="Place Order", font=("Helvetica", 14), bg="#28a745", fg="white", command=self.place_order)
        self.place_order_btn.pack(pady=20)

    def animate_gif(self, index):
        self.canvas.itemconfig(self.image_on_canvas, image=self.sequence[index])
        self.root.after(100, self.animate_gif, (index + 1) % len(self.sequence))

    def show_main_page(self):
        pygame.mixer.Sound("click.wav").play()  # Play click sound

        self.customer_name = self.name_entry.get().strip()
        self.customer_phone = self.phone_entry.get().strip()

        if not self.customer_name or self.customer_name.startswith("What's"):
            messagebox.showwarning("Missing Name", "Please enter your name first!")
            return

        if not self.customer_phone.startswith("+91") or len(self.customer_phone) != 13:
            messagebox.showwarning("Invalid Phone", "Please enter a valid phone number in format +91XXXXXXXXXX")
            return

        self.home_frame.pack_forget()
        self.title_label.config(text=f"Welcome, {self.customer_name} ☕")
        self.main_frame.pack(fill="both", expand=True)

    def create_item(self, code, item):
        frame = tk.Frame(self.items_frame, bg="#333")
        frame.pack(fill="x", padx=10, pady=5)

        label = tk.Label(frame, text=f"{item['name']} (₹{item['price']})", font=("Helvetica", 12), fg="white", bg="#333")
        label.pack(side="left", padx=10)

        qty_var = tk.IntVar()
        qty_spin = tk.Spinbox(frame, from_=0, to=10, width=5, textvariable=qty_var, font=("Helvetica", 12))
        qty_spin.pack(side="right", padx=10)

        self.order[code] = qty_var

    def place_order(self):
        final_order = {}
        for code, qty_var in self.order.items():
            qty = qty_var.get()
            if qty > 0:
                final_order[code] = qty

        if not final_order:
            messagebox.showwarning("Empty Order", "Please select at least one item.")
            return

        total = calculate_total(final_order)
        readable_order = {coffee_menu[code]['name']: qty for code, qty in final_order.items()}
        order_id = save_order(readable_order, total)

        # Include quantity for receipt generation
        receipt_data = {}
        for code, qty in final_order.items():
            item = coffee_menu[code]
            receipt_data[code] = {
                'name': item['name'],
                'price': item['price'],
                'qty': qty
            }

        generate_receipt(order_id, receipt_data, total)

        self.total_label.config(text=f"Total: ₹{total}")

        # WhatsApp message sending
        message = f"HAVOC Coffee Order ID: {order_id}\nTotal: ₹{total}\nThank you for ordering!"
        send_whatsapp_message(self.customer_phone, message)

        messagebox.showinfo("Order Placed", f"Your order ID is {order_id}\nReceipt saved and WhatsApp message sent!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HavocApp(root)
    root.mainloop()
    