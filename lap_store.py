import tkinter as tk
from tkinter import messagebox
import mysql.connector as mc

mysqldb = mc.connect(host="localhost", user="root",
                     password="", database="laptopstoredb")
mysqlcursor = mysqldb.cursor()
mysqldb.commit()
# mysqlcursor.execute("CREATE TABLE orders (Order_id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(30), Contact_Number VARCHAR(10), Email_id VARCHAR(30), Address VARCHAR(50))")

# mysqlcursor.execute("CREATE TABLE ordered_laptop (Order_id INT, Laptop_Name VARCHAR(150), Laptop_Price INT, FOREIGN KEY (Order_id) REFERENCES orders(Order_id))")


class Laptop:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ECommerce:
    def __init__(self, root):
        self.root = root
        self.root.title("Laptop Store")
        self.root.geometry("500x500")
        self.products = [
            Laptop("Lenovo Ideapad", 50000),
            Laptop("Asus Zenbook 14", 120000),
            Laptop("Dell Inspiron", 85000),
            Laptop("Asus TUF A15", 90000),
            Laptop("Gigabyte Gaming", 74000),
            Laptop("Lenovo Legion", 153000),
            Laptop("Dell Alienware", 278000),
            Laptop("Asus ROG Strix G16", 180000),
            Laptop("Lenovo Ideapad Gaming", 65000),
            Laptop("HP Omen", 200000),
            Laptop("HP Victus", 80000),
            Laptop("Acer Aspire", 55000),
            Laptop("Acer Predator Helios 16", 165000)
        ]

        self.cart = []
        self.customer_info = {
            "Name": tk.StringVar(),
            "Email": tk.StringVar(),
            "Ph. No.": tk.StringVar(),
            "Address": tk.StringVar()
        }

        self.create_button()

    def create_button(self):
        self.laptops = tk.Listbox(self.root, width=400, height=20)
        for laptop in self.products:
            self.laptops.insert(tk.END, f"{laptop.name} - Rs{laptop.price}")
        self.laptops.pack(padx=10, pady=10)

        atc_button = tk.Button(self.root, text="Add to Cart", command=self.atc)
        atc_button.pack(pady=5)

        vc_button = tk.Button(self.root, text="View My Cart", command=self.vc)
        vc_button.pack(pady=5)

    def atc(self):
        sel_laptop = self.laptops.curselection()
        if sel_laptop:
            laptop = self.products[sel_laptop[0]]
            self.cart.append(laptop)
            messagebox.showinfo(
                "Added to Cart", f"{laptop.name} added to your cart!")

    def vc(self):
        if not self.cart:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")
        else:
            self.cust_details()

    def cust_details(self):
        cust_ent = tk.Toplevel(self.root, width=40)
        cust_ent.title("Customer Deatils")
        cust_ent.geometry("300x200")

        tk.Label(cust_ent, text="Name :").grid(row=0, column=0)
        tk.Entry(cust_ent, textvariable=self.customer_info["Name"]).grid(
            row=0, column=1)

        tk.Label(cust_ent, text="Email :").grid(row=1, column=0)
        tk.Entry(cust_ent, textvariable=self.customer_info["Email"]).grid(
            row=1, column=1)

        tk.Label(cust_ent, text="Ph. No. :").grid(row=2, column=0)
        tk.Entry(cust_ent, textvariable=self.customer_info["Ph. No."]).grid(
            row=2, column=1)

        tk.Label(cust_ent, text="Address :").grid(row=3, column=0)
        tk.Entry(cust_ent, textvariable=self.customer_info["Address"]).grid(
            row=3, column=1)

        confirm_button = tk.Button(
            cust_ent, text="Confirm", command=self.confirm_order)
        confirm_button.grid(row=4, column=0, columnspan=2, pady=10)

    def confirm_order(self):
        order_details = tk.Toplevel(self.root)
        order_details.title("Order Confirmation")
        order_details.geometry("600x400")

        name = self.customer_info["Name"].get()
        email = self.customer_info["Email"].get()
        mobile = self.customer_info["Ph. No."].get()
        address = self.customer_info["Address"].get()

        order = f"Customer Details:\nName: {name}\nEmail: {email}\nPh. No : {mobile}\nAddress: {address}\n"
        tk.Label(order_details, text=order).pack(padx=10, pady=10)

        self.cart_items = tk.Listbox(order_details, width=80, height=3)
        for i in self.cart:
            self.cart_items.insert(tk.END, f"{i.name} - Rs{i.price}")
        self.cart_items.pack(padx=10, pady=10)

        total_price = sum([laptop.price for laptop in self.cart])
        totalprice = f"\n\nTotal Price: Rs{total_price}\n"
        self.tp = tk.Label(order_details, text=totalprice)
        self.tp.pack(padx=10, pady=10)

        pob = tk.Button(
            order_details, text="Place Order", command=self.place_order)
        pob.pack(padx=10, pady=10)

        dib = tk.Button(
            order_details, text="Delete item/s", command=self.del_item)
        dib.pack(padx=10, pady=10)

    def place_order(self):
            name = self.customer_info["Name"].get()
            email = self.customer_info["Email"].get()
            mobile = self.customer_info["Ph. No."].get()
            address = self.customer_info["Address"].get()

            mysqlcursor.execute("INSERT INTO orders (Name, Contact_Number, Email_id,Address) VALUES (%s, %s, %s, %s)", (name, mobile, email, address))

            order_id = mysqlcursor.lastrowid
            for l in self.cart:
                mysqlcursor.execute("INSERT INTO ordered_laptop(Order_id, Laptop_Name, Laptop_Price) VALUES (%s, %s, %s)", (order_id, l.name, l.price))
                mysqldb.commit()
            mysqldb.close()

            messagebox.showinfo("Order Confirmed", "Thank U! Visit Again!!")
            self.root.destroy()

    def del_item(self):
        sel_laptop = self.cart_items.curselection()
        laptop = self.cart[sel_laptop[0]]
        self.cart.remove(laptop)
        messagebox.showinfo("Removed from Cart",
                            "Selected item removed from your cart.")

        self.updatecart()

    def updatecart(self):
        self.cart_items.delete(0, tk.END)
        for laptop in self.cart:
            self.cart_items.insert(tk.END, f"{laptop.name} - Rs{laptop.price}")

        self.updateprice()

    def updateprice(self):
        total_price = sum([laptop.price for laptop in self.cart])
        totalprice = f"\n\nTotal Price: Rs{total_price}\n"
        self.tp.config(text=totalprice)


if __name__ == "__main__":
    root = tk.Tk()
    a = ECommerce(root)
    root.mainloop()
