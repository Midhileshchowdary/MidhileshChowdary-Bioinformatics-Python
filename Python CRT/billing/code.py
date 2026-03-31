from tkinter import *
from tkinter import messagebox
import random
import os

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        self.root.config(bg="lightblue")

        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg="blue", fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # === Variables ===
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Product variables
        self.med1 = IntVar()
        self.med2 = IntVar()
        self.med3 = IntVar()

        self.groc1 = IntVar()
        self.groc2 = IntVar()
        self.groc3 = IntVar()

        self.cold1 = IntVar()
        self.cold2 = IntVar()
        self.cold3 = IntVar()

        # Price variables
        self.med_price = StringVar()
        self.groc_price = StringVar()
        self.cold_price = StringVar()

        self.med_tax = StringVar()
        self.groc_tax = StringVar()
        self.cold_tax = StringVar()

        # === Customer Details Frame ===
        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold", bg="lightblue", bd=10, relief=GROOVE)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, font="arial 13", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phone, font="arial 13", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, textvariable=self.search_bill, font="arial 13", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10, pady=10)

        # === Product Frames ===

        # Medical
        F2 = LabelFrame(self.root, text="Medical Products", bd=10, relief=GROOVE, bg="lightblue", font=("times new roman", 15, "bold"), fg="gold")
        F2.place(x=5, y=180, width=325, height=380)

        m1 = Label(F2, text="Paracetamol", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        m1_txt = Entry(F2, width=10, textvariable=self.med1, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        m2 = Label(F2, text="Cough Syrup", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        m2_txt = Entry(F2, width=10, textvariable=self.med2, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        m3 = Label(F2, text="Antibiotic", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        m3_txt = Entry(F2, width=10, textvariable=self.med3, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        # Grocery
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, bg="lightblue", font=("times new roman", 15, "bold"), fg="gold")
        F3.place(x=340, y=180, width=325, height=380)

        g1 = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.groc1, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2 = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.groc2, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3 = Label(F3, text="Oil", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.groc3, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        # Cold Drinks
        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, bg="lightblue", font=("times new roman", 15, "bold"), fg="gold")
        F4.place(x=670, y=180, width=325, height=380)

        c1 = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.cold1, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2 = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.cold2, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3 = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.cold3, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        # === Bill Area ===
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=340, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # === Button Frame ===
        F6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold", bg="lightblue", bd=10, relief=GROOVE)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_btn = Button(F6, text="Total", command=self.total, width=12, font="arial 14 bold", bd=7, bg="cadetblue", fg="white").grid(row=0, column=0, padx=20, pady=10)
        m2_btn = Button(F6, text="Generate Bill", command=self.bill_area, width=12, font="arial 14 bold", bd=7, bg="cadetblue", fg="white").grid(row=0, column=1, padx=20, pady=10)
        m3_btn = Button(F6, text="Clear", command=self.clear_data, width=12, font="arial 14 bold", bd=7, bg="cadetblue", fg="white").grid(row=0, column=2, padx=20, pady=10)
        m4_btn = Button(F6, text="Exit", command=self.exit_app, width=12, font="arial 14 bold", bd=7, bg="cadetblue", fg="white").grid(row=0, column=3, padx=20, pady=10)

        self.welcome_bill()

    def total(self):
        self.total_med_price = (self.med1.get()*50 + self.med2.get()*100 + self.med3.get()*200)
        self.med_tax.set(f"₹ {self.total_med_price*0.05:.2f}")

        self.total_groc_price = (self.groc1.get()*60 + self.groc2.get()*50 + self.groc3.get()*80)
        self.groc_tax.set(f"₹ {self.total_groc_price*0.1:.2f}")

        self.total_cold_price = (self.cold1.get()*40 + self.cold2.get()*45 + self.cold3.get()*30)
        self.cold_tax.set(f"₹ {self.total_cold_price*0.05:.2f}")

        self.total_price = self.total_med_price + self.total_groc_price + self.total_cold_price
        self.total_tax = (self.total_med_price*0.05 + self.total_groc_price*0.1 + self.total_cold_price*0.05)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to ABC Retail\n")
        self.txtarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=====================================")
        self.txtarea.insert(END, f"\nProduct\t\tQty\tPrice")
        self.txtarea.insert(END, f"\n=====================================\n")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
            return

        self.welcome_bill()

        products = [
            ("Paracetamol", self.med1.get(), 50),
            ("Cough Syrup", self.med2.get(), 100),
            ("Antibiotic", self.med3.get(), 200),
            ("Rice", self.groc1.get(), 60),
            ("Wheat", self.groc2.get(), 50),
            ("Oil", self.groc3.get(), 80),
            ("Sprite", self.cold1.get(), 40),
            ("Thumbs Up", self.cold2.get(), 45),
            ("Frooti", self.cold3.get(), 30),
        ]

        for prod, qty, price in products:
            if qty > 0:
                self.txtarea.insert(END, f"\n{prod}\t\t{qty}\t{qty*price}")

        self.txtarea.insert(END, f"\n-------------------------------------")
        self.txtarea.insert(END, f"\nTotal Tax:\t\t\t₹ {self.total_tax:.2f}")
        self.txtarea.insert(END, f"\nTotal Amount:\t\t\t₹ {self.total_price + self.total_tax:.2f}")
        self.txtarea.insert(END, f"\n-------------------------------------")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op:
            bill_data = self.txtarea.get('1.0', END)
            if not os.path.exists("bills"):
                os.makedirs("bills")
            with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
                f.write(bill_data)
            messagebox.showinfo("Saved", f"Bill {self.bill_no.get()} saved successfully")

    def find_bill(self):
        try:
            with open(f"bills/{self.search_bill.get()}.txt", "r") as f:
                self.txtarea.delete("1.0", END)
                for line in f:
                    self.txtarea.insert(END, line)
        except FileNotFoundError:
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear_data(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill.set("")
        self.med1.set(0)
        self.med2.set(0)
        self.med3.set(0)
        self.groc1.set(0)
        self.groc2.set(0)
        self.groc3.set(0)
        self.cold1.set(0)
        self.cold2.set(0)
        self.cold3.set(0)
        self.welcome_bill()

    def exit_app(self):
        self.root.destroy()

# === Main Loop ===
root = Tk()
obj = BillingApp(root)
root.mainloop()
