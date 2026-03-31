# BudgetBuddy with Enhanced Tkinter GUI, Calendar, and Monthly Budget (Now with Real-Time Summary)

import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk

# ---------------------- DATABASE SETUP ----------------------
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    user TEXT,
                    category TEXT,
                    amount REAL,
                    date TEXT,
                    recurring INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                    user TEXT,
                    month TEXT,
                    amount REAL)''')
conn.commit()

# ---------------------- CLASSES ----------------------

class Expense:
    def __init__(self, user, category, amount, date, recurring=False):
        self.user = user
        self.category = category
        self.amount = amount
        self.date = date
        self.recurring = recurring

    def save(self):
        cursor.execute("INSERT INTO expenses (user, category, amount, date, recurring) VALUES (?, ?, ?, ?, ?)",
                       (self.user, self.category, self.amount, self.date, int(self.recurring)))
        conn.commit()

class BudgetBuddy:
    def __init__(self, user):
        self.user = user

    def add_expense(self, category, amount, date, recurring=False):
        amount = float(amount)
        Expense(self.user, category, amount, date, recurring).save()

    def set_monthly_budget(self, month, amount):
        cursor.execute("REPLACE INTO budgets (user, month, amount) VALUES (?, ?, ?)", (self.user, month, amount))
        conn.commit()

    def get_monthly_budget(self, month):
        cursor.execute("SELECT amount FROM budgets WHERE user=? AND month=?", (self.user, month))
        result = cursor.fetchone()
        return float(result[0]) if result else 0.0

    def summary(self, date=None):
        df = pd.read_sql_query("SELECT * FROM expenses WHERE user=?", conn, params=(self.user,))
        if date:
            df['date'] = pd.to_datetime(df['date'])
            df = df[df['date'] == pd.to_datetime(date)]
        if df.empty:
            messagebox.showinfo("Info", "No expenses to display.")
            return
        summary = df.groupby('category')['amount'].sum()
        summary.plot.pie(autopct='%1.1f%%', title='Expense Distribution', ylabel='')
        plt.tight_layout()
        plt.show()

    def monthly_trend(self, start_date=None, end_date=None):
        df = pd.read_sql_query("SELECT * FROM expenses WHERE user=?", conn, params=(self.user,))
        df['date'] = pd.to_datetime(df['date'])
        if start_date and end_date:
            df = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]
        df['month'] = df['date'].dt.to_period('M')
        trend = df.groupby('month')['amount'].sum()
        if trend.empty:
            messagebox.showinfo("Info", "No data for selected range.")
            return
        trend.plot(kind='bar', title='Monthly Expenses')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.tight_layout()
        plt.show()

    def calculate_remaining_budget(self, current_month):
        total_budget = self.get_monthly_budget(current_month)
        df = pd.read_sql_query("SELECT * FROM expenses WHERE user=?", conn, params=(self.user,))
        df['date'] = pd.to_datetime(df['date'])
        df = df[df['date'].dt.to_period('M') == pd.Period(current_month)]
        spent = df['amount'].sum()
        remaining = total_budget - spent
        messagebox.showinfo("Remaining Budget", f"Remaining budget for {current_month}: ₹{remaining:.2f}")

# ---------------------- GUI ----------------------

def run_gui():
    root = tk.Tk()
    root.title("BudgetBuddy")
    root.geometry("700x700")
    root.configure(bg="lightblue")

    tk.Label(root, text="Enter your name:", bg="lightblue", font=("Arial", 12)).pack(pady=5)
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)

    tk.Label(root, text="Select date range to view summary:", bg="lightblue", font=("Arial", 12)).pack(pady=5)

    cal_frame = tk.Frame(root, bg="lightblue")
    cal_frame.pack()

    tk.Label(cal_frame, text="Start Date:", bg="lightblue").grid(row=0, column=0)
    cal_start = Calendar(cal_frame, selectmode='day')
    cal_start.grid(row=1, column=0, padx=10)

    tk.Label(cal_frame, text="End Date:", bg="lightblue").grid(row=0, column=1)
    cal_end = Calendar(cal_frame, selectmode='day')
    cal_end.grid(row=1, column=1, padx=10)

    def view_summary():
        user = name_entry.get()
        if not user:
            messagebox.showerror("Error", "Enter your name.")
            return
        start_date = cal_start.get_date()
        end_date = cal_end.get_date()
        app = BudgetBuddy(user)
        app.monthly_trend(start_date, end_date)

    def view_pie():
        user = name_entry.get()
        if not user:
            messagebox.showerror("Error", "Enter your name.")
            return
        start_date = cal_start.get_date()
        app = BudgetBuddy(user)
        app.summary(start_date)

    def open_add_expense():
        user = name_entry.get()
        if not user:
            messagebox.showerror("Error", "Enter your name.")
            return

        app = BudgetBuddy(user)

        win = tk.Toplevel(root)
        win.title("Add Expense")
        win.geometry("400x300")

        tk.Label(win, text="Date:").pack()
        date_cal = Calendar(win, selectmode='day')
        date_cal.pack()

        tk.Label(win, text="Category:").pack()
        category = tk.Entry(win)
        category.pack()

        tk.Label(win, text="Amount:").pack()
        amount = tk.Entry(win)
        amount.pack()

        recur_var = tk.IntVar()
        tk.Checkbutton(win, text="Recurring", variable=recur_var).pack()

        def save():
            dt = datetime.strptime(date_cal.get_date(), "%m/%d/%y")
            date_str = dt.strftime("%Y-%m-%d")
            month_key = dt.strftime("%Y-%m")

            if app.get_monthly_budget(month_key) == 0.0:
                budget_amt = simpledialog.askfloat("Monthly Budget", f"Enter budget for {month_key}:")
                if budget_amt:
                    app.set_monthly_budget(month_key, budget_amt)

            app.add_expense(category.get(), amount.get(), date_str, bool(recur_var.get()))
            messagebox.showinfo("Saved", "Expense added successfully!")

        tk.Button(win, text="Save Expense", command=save).pack(pady=10)

    tk.Button(root, text="Add Expense", command=open_add_expense).pack(pady=10)
    tk.Button(root, text="View Pie Chart for Start Date", command=view_pie).pack(pady=5)
    tk.Button(root, text="View Summary Graph", command=view_summary).pack(pady=5)

    root.mainloop()

# ---------------------- RUN ----------------------
if __name__ == '__main__':
    run_gui()
