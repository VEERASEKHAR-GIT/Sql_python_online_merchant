import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect("database_setup.sql")
cursor = conn.cursor()

# Create the Categories table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
""")

# Create the Products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL,
        category_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)
    )
""")

# Create the Customers table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Create the Orders table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL,
        total_price REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
""")

# Create the OrderItems table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS OrderItems (
        order_item_id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        unit_price REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    )
""")

# Create the Payments table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Payments (
        payment_id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL,
        payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        payment_method TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id)
    )
""")

# Create the Addresses table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Addresses (
        address_id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        street_address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        postal_code TEXT NOT NULL,
        country TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
""")

# Save changes and close the connection
conn.commit()
conn.close()
#veerasekhar
