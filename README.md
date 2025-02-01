Laptop Store E-Commerce Application
A simple Python-based desktop application for an e-commerce store that sells laptops. The application allows users to browse laptops, add them to their cart, provide customer details, and place an order. The application uses a graphical user interface (GUI) built with Tkinter and interacts with a MySQL database to store order details.

Features
Browse Laptops: View a list of available laptops along with their prices.
Add to Cart: Select laptops and add them to your cart.
View Cart: Review the items in your cart, update the cart by removing items, and see the total price.
Enter Customer Information: Provide customer details such as name, email, phone number, and address.
Place an Order: Confirm the order, which will be stored in a MySQL database.
Database Integration: Store customer details and ordered laptops in a MySQL database.
Technologies Used
Python: Core programming language used for building the application.
Tkinter: A built-in Python library used for creating the GUI.
MySQL: The database used to store order and laptop details.
MySQL Connector (mysql-connector-python): Used to interact with the MySQL database from Python.
Prerequisites
To run this project on your local machine, ensure you have the following:

Python (version 3.x or higher)

MySQL installed and running on your machine.

MySQL Connector for Python (mysql-connector-python)

You can install the MySQL Connector using pip:
**pip install mysql-connector-python**
Tkinter (comes pre-installed with Python)

Setting Up the Database
Before running the application, you need to set up the MySQL database.

Create the Database:

Open your MySQL client and create a database named laptopstoredb:
**CREATE DATABASE laptopstoredb;
Create the Orders Table:**

This table will store the order information, such as customer name, phone number, email, and address.
**CREATE TABLE orders (
  Order_id INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(30),
  Contact_Number VARCHAR(10),
  Email_id VARCHAR(30),
  Address VARCHAR(50)
);**
Create the Ordered Laptop Table:

This table will store details about the laptops ordered, and it has a foreign key referencing the orders table.
**CREATE TABLE ordered_laptop (
  Order_id INT,
  Laptop_Name VARCHAR(150),
  Laptop_Price INT,
  FOREIGN KEY (Order_id) REFERENCES orders(Order_id)
);**
How to Run the Application
Clone the Repository:

**git clone https://github.com/yourusername/laptop-store-ecommerce.git
cd laptop-store-ecommerce**
Configure MySQL Connection: In the Python file (main.py or the script file), make sure to update the MySQL connection details to match your local MySQL setup:

**mysqldb = mc.connect(host="localhost", user="your-username", password="your-password", database="laptopstoredb")**

Run the Application: Run the Python script:
**python main.py**

Future Enhancements
User Login and Registration: Add user authentication and profile management.
Improved Cart Management: Allow for quantity selection of laptops.
Order History: Display past orders from the database.
Real-time Price Updates: Fetch laptop prices dynamically from an API.
