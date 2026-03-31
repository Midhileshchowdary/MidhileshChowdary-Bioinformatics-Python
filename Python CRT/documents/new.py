import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import tempfile
import platform
import subprocess
import os
import threading

# --- Database Setup ---
def setup_db():
    conn = sqlite3.connect('inventoryease.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    gst_percent REAL NOT NULL,
                    product_type TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS invoices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    total REAL NOT NULL,
                    total_gst REAL NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS invoice_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    invoice_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY(invoice_id) REFERENCES invoices(id),
                    FOREIGN KEY(product_id) REFERENCES products(id)
                )''')
    conn.commit()
    conn.close()

# --- Product Management ---
def add_product_db(name, price, stock, gst, ptype):
    conn = sqlite3.connect('inventoryease.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (name, price, stock, gst_percent, product_type) VALUES (?, ?, ?, ?, ?)",
              (name, price, stock, gst, ptype))
    conn.commit()
    conn.close()

def fetch_products_db():
    conn = sqlite3.connect('inventoryease.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    conn.close()
    return rows

def update_stock_batch(items, cursor):
    for product_id, qty in items:
        cursor.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (qty, product_id))

# --- Invoice Management ---
def create_invoice_db(date, total, total_gst, items):
    conn = sqlite3.connect('inventoryease.db')
    c = conn.cursor()
    c.execute("INSERT INTO invoices (date, total, total_gst) VALUES (?, ?, ?)", (date, total, total_gst))
    invoice_id = c.lastrowid
    c.executemany("INSERT INTO invoice_items (invoice_id, product_id, quantity) VALUES (?, ?, ?)",
                  [(invoice_id, product_id, qty) for product_id, qty in items])
    update_stock_batch(items, c)
    conn.commit()
    conn.close()
    return invoice_id

# --- GUI Application ---
class InventoryEaseApp(tk.Tk):
    def __init__(self):  # ✅ Fixed Constructor
        super().__init__()
        self.title("InventoryEase - Inventory & Billing System")
        self.geometry("950x650")
        self.configure(bg="#34495e")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
        self.style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"), background="#2c3e50", foreground="white")
        self.style.map('Treeview', background=[('selected', '#1abc9c')])

        self.create_sidebar()
        self.create_main_area()
        self.load_products()
        self.cart = []

    def create_sidebar(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=180)
        self.sidebar.pack(side="left", fill="y")

        title = tk.Label(self.sidebar, text="InventoryEase", bg="#2c3e50",
                         fg="white", font=("Segoe UI", 22, "bold"))
        title.pack(pady=30)

        buttons = [
            ("Add Product", self.show_add_product),
            ("Create Invoice", self.show_create_invoice),
            ("View Products", self.show_view_products),
            ("Exit", self.quit)
        ]

        for (text, cmd) in buttons:
            btn = tk.Button(self.sidebar, text=text, command=cmd,
                            bg="#34495e", fg="white", relief="flat",
                            font=("Segoe UI", 14), pady=12)
            btn.pack(fill="x", padx=10, pady=6)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1abc9c"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#34495e"))

    def create_main_area(self):
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.frame_add_product = tk.Frame(self.main_frame, bg="white", padx=30, pady=30)
        self.frame_create_invoice = tk.Frame(self.main_frame, bg="white", padx=20, pady=20)
        self.frame_view_products = tk.Frame(self.main_frame, bg="white", padx=20, pady=20)

        self.create_add_product_ui()
        self.create_create_invoice_ui()
        self.create_view_products_ui()

        self.show_add_product()

    # --- Add Product UI ---
    def create_add_product_ui(self):
        frame = self.frame_add_product

        tk.Label(frame, text="Add New Product", font=("Segoe UI", 20, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))
        labels = ["Product Name:", "Price:", "Stock:", "GST %:", "Product Type:"]
        for i, text in enumerate(labels):
            tk.Label(frame, text=text, font=("Segoe UI", 14), bg="white").grid(row=i+1, column=0, sticky="e", pady=10, padx=10)

        self.name_entry = tk.Entry(frame, font=("Segoe UI", 14), width=30)
        self.name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.price_entry = tk.Entry(frame, font=("Segoe UI", 14), width=30)
        self.price_entry.grid(row=2, column=1, pady=10, padx=10)
        self.stock_entry = tk.Entry(frame, font=("Segoe UI", 14), width=30)
        self.stock_entry.grid(row=3, column=1, pady=10, padx=10)
        self.gst_entry = tk.Entry(frame, font=("Segoe UI", 14), width=30)
        self.gst_entry.grid(row=4, column=1, pady=10, padx=10)
        self.gst_entry.insert(0, "18")
        self.type_combo = ttk.Combobox(frame, values=["Physical", "Digital"], font=("Segoe UI", 14), state="readonly", width=28)
        self.type_combo.grid(row=5, column=1, pady=10, padx=10)
        self.type_combo.current(0)

        add_btn = ttk.Button(frame, text="Add Product", command=self.add_product)
        add_btn.grid(row=6, column=0, columnspan=2, pady=25)

    def add_product(self):
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        gst = self.gst_entry.get().strip()
        ptype = self.type_combo.get()

        if not name:
            messagebox.showerror("Input Error", "Product name is required.")
            return
        try:
            price = float(price)
            stock = int(stock)
            gst = float(gst)
        except ValueError:
            messagebox.showerror("Input Error", "Price, Stock, and GST must be numeric.")
            return

        add_product_db(name, price, stock, gst, ptype)
        messagebox.showinfo("Success", f"Product '{name}' added successfully!")
        self.clear_add_form()
        self.load_products()

    def clear_add_form(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.gst_entry.delete(0, tk.END)
        self.gst_entry.insert(0, "18")
        self.type_combo.current(0)

    def show_add_product(self):
        self.frame_create_invoice.pack_forget()
        self.frame_view_products.pack_forget()
        self.frame_add_product.pack(expand=True, fill="both")

    # --- View Products UI ---
    def create_view_products_ui(self):
        frame = self.frame_view_products
        tk.Label(frame, text="Product List", font=("Segoe UI", 20, "bold"), bg="white").pack(pady=10)

        columns = ("ID", "Name", "Price", "Stock", "GST%", "Type")
        tree_frame = tk.Frame(frame)
        tree_frame.pack(expand=True, fill="both", pady=10, padx=10)

        self.tree_products = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.tree_products.heading(col, text=col)
            self.tree_products.column(col, anchor="center", width=100)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree_products.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree_products.xview)
        self.tree_products.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree_products.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

    def load_products(self):
        if hasattr(self, 'tree_products'):
            for row in self.tree_products.get_children():
                self.tree_products.delete(row)
            products = fetch_products_db()
            for prod in products:
                self.tree_products.insert("", "end", values=prod)

    def show_view_products(self):
        self.frame_add_product.pack_forget()
        self.frame_create_invoice.pack_forget()
        self.frame_view_products.pack(expand=True, fill="both")
        self.load_products()

    # --- Create Invoice UI ---
    def create_create_invoice_ui(self):
        # You can paste this block from your original code if needed
        pass

    def show_create_invoice(self):
        # You can paste this block from your original code if needed
        pass

    # Add the rest of the invoice methods below as in your previous script

# --- Run Application ---
if __name__ == "__main__":  # ✅ Corrected Entry Point
    setup_db()
    app = InventoryEaseApp()
    app.mainloop()
