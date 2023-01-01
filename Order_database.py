import sqlite3
conn = sqlite3.connect("Order.db")
c= conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS customers(
    customerID INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName TEXT,
    lastName TEXT,
    address TEXT,
    postcode TEXT
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS product(
    productID INTEGER PRIMARY KEY AUTOINCREMENT,
    productName TEXT,
    price REAL
)
""")
c.execute("PRAGMA foreign_keys = ON")
c.execute("""
CREATE TABLE IF NOT EXISTS orders(
    orderID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerID INTEGER,
    orderDate DATE,
    FOREIGN KEY(customerID) REFERENCES customers(customerID)
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS orderDetails(
    orderID INTEGER,
    productID INTEGER,
    quantity INTEGER,
    PRIMARY KEY(orderID, productID)
    FOREIGN KEY(orderID) REFERENCES orders(orderID)
    FOREIGN KEY(productID) REFERENCES product(productID)
)
""")
conn.commit()
conn.close()

def addCustomer(firstName, lastName, address, postcode):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    INSERT INTO customers(firstName, lastName, address, postcode)
    VALUES (?, ?, ?, ?)
    """,(firstName, lastName, address, postcode))
    conn.commit()
    conn.close()
#addCustomer("Sam", "Smith", "11 square road", "SD5 678")

def updateCustomer(customerID, firstName, lastName, address, postcode):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    UPDATE customers
    SET firstName = ?, lastName = ?, address = ?, postcode = ?
    WHERE customerID = ?
    """,(firstName, lastName, address, postcode, customerID))
    conn.commit()
    conn.close()
#updateCustomer(1, "Bob", "Smith", "20 circle road", "SD5 678")

def deleteCustomer(customerID):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    DELETE FROM customers
    WHERE customerID = ?
    """,(customerID,))
    conn.commit()
    conn.close()
#deleteCustomer(1)

def addProduct(productName, price):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    INSERT INTO product(productName, price)
    VALUES (?, ?)
    """,(productName, price))
    conn.commit()
    conn.close()
#addProduct("orange", 3.50)

def updateProduct(productID, productName, price):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    UPDATE product
    SET productName = ?, price = ?
    WHERE productID = ?
    """,(productName, price, productID))
    conn.commit()
    conn.close()

def deleteProduct(productID):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    DELETE FROM product
    WHERE productID = ?
    """,(productID,))
    conn.commit()
    conn.close()

def addOrder(customerID, orderDate):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("""
    INSERT INTO orders(customerID, orderDate)
    VALUES (?, ?)
    """,(customerID, orderDate))
    conn.commit()
    conn.close()
addOrder(2, "2022-03-19")

def deleteOrder(orderID):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("""
    DELETE FROM orders
    WHERE orderID = ?
    """,(orderID,))
    conn.commit()
    conn.close()

def addOrderDetails(orderID, productID, quantity):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("""
    INSERT INTO orderDetails
    VALUES (?, ?, ?)
    """,(orderID, productID, quantity))
    conn.commit()
    conn.close()
#addOrderDetails(1, 2, 3)

def deleteOrderDetails(orderID, productID):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    c.execute("""
    DELETE FROM orderDetails
    WHERE orderID = ? AND productID = ?
    """,(orderID, productID))
    conn.commit()
    conn.close()

def updateOrderDetails(orderID, productID, quantity):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    UPDATE orderDetails
    SET quantity = ?
    WHERE orderID = ?, productID = ?
    """,(quantity, orderID, productID))
    conn.commit()
    conn.close()

def getOrderByID(orderID):
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    SELECT product.productName, orderDetails.quantity
    FROM product
    JOIN orderDetails
    ON product.productID = orderDetails.productID
    WHERE orderDetails.orderID = ?
    """,(orderID,))
    query = c.fetchall()
    print(query)
    conn.close()
#getOrderByID(1)

def getProducts():
    conn = sqlite3.connect("Order.db")
    c= conn.cursor()
    c.execute("""
    SELECT productName, price
    FROM product
    """)
    query = c.fetchall()
    conn.close()
    return query


# conn = sqlite3.connect("Order.db")
# c= conn.cursor()
# c.execute("""
#    SELECT customers.firstName, orders.orderDate
#    FROM customers
#    JOIN orders
#    ON customers.customerID = orders.customerID
#    WHERE customers.customerID = 2 
# """)
# query = c.fetchall()
# print(query)


# conn.commit()
# conn.close()