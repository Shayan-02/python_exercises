import sqlite3


def connect():
    """
    Establishes a connection to the SQLite database and creates a table 'product'
    if it does not already exist.
    The table has the following columns:
    - id: Integer (Primary Key, Auto Incremented)
    - name: Text (Product Name)
    - quantity: Integer (Product Quantity)
    - price: Real (Product Price)
    """
    con = sqlite3.connect("store.db")  # Connect to the database (or create it)
    cur = con.cursor()  # Create a cursor object to execute SQL commands
    cur.execute(
        """CREATE TABLE IF NOT EXISTS product 
                   (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)"""
    )
    con.commit()  # Save (commit) the changes
    con.close()  # Close the connection to the database


def insert(name, quantity, price):
    """
    Inserts a new product into the 'product' table.

    Parameters:
    - name (str): Name of the product.
    - quantity (int): Quantity of the product.
    - price (float): Price of the product.
    """
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO product VALUES (NULL, ?, ?, ?)", (name, quantity, price)
    )  # Insert the product into the table
    con.commit()
    con.close()


def view():
    """
    Fetches and returns all products from the 'product' table.

    Returns:
    - rows (list of tuples): A list of all product records.
    """
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM product")  # Fetch all records from the 'product' table
    rows = cur.fetchall()  # Fetch all the results
    con.close()
    return rows


def search(name="", quantity="", price=""):
    """
    Searches for products based on the provided name, quantity, or price.
    If multiple parameters are provided, it performs an OR search.

    Parameters:
    - name (str): Name of the product to search for (default: "").
    - quantity (int): Quantity of the product to search for (default: "").
    - price (float): Price of the product to search for (default: "").

    Returns:
    - rows (list of tuples): A list of matching product records.
    """
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM product WHERE name=? OR quantity=? OR price=?",
        (name, quantity, price),
    )
    rows = cur.fetchall()  # Fetch the matching records
    con.close()
    return rows


def delete(id):
    """
    Deletes a product from the 'product' table based on its ID.

    Parameters:
    - id (int): ID of the product to be deleted.
    """
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute(
        "DELETE FROM product WHERE id=?", (id,)
    )  # Delete the product with the specified ID
    con.commit()
    con.close()


def update(id, name, quantity, price):
    """
    Updates the details of a product in the 'product' table based on its ID.

    Parameters:
    - id (int): ID of the product to be updated.
    - name (str): New name of the product.
    - quantity (int): New quantity of the product.
    - price (float): New price of the product.
    """
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE product SET name=?, quantity=?, price=? WHERE id=?",
        (name, quantity, price, id),
    )
    con.commit()  # Save the changes
    con.close()


# Connect to the database and ensure the table is created
connect()
