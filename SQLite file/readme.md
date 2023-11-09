# SQLite
---
SQLite is a popular, lightweight, and self-contained relational database management system (RDBMS) that you can use with Python. It's often used in embedded systems, mobile applications, and desktop software. In this guide, I'll walk you through the basic steps to use SQLite with Python.
### 1. Install SQLite:
SQLite is included with Python, so you don't need to install it separately.
### 2. Import the SQLite Library:
To use SQLite in Python, you need to import the sqlite3 library.
```py
import sqlite3
```
### 3. Connect to a Database:
To work with an SQLite database, you need to establish a connection to it. You can either connect to an existing database file or create a new one.
```py
# Connect to an existing database or create a new one if it doesn't exist
conn = sqlite3.connect('mydatabase.db')
```
### 4. Create a Cursor:
To execute SQL commands, you'll need to create a cursor object.
```py
cursor = conn.cursor()
```
### 5.Execute SQL Commands:
You can use the cursor to execute SQL commands. Here are some common operations:
- Creating a Table:
  
  ```py
  cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (name TEXT, salary REAL)''')
  # data type : null, integer, real, text ....                
  conn.commit()
  ```
- Inserting Data:
  
  ```py
  cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ("John Doe", 50000))
  conn.commit()
  ```
- Inserting Multiple Rows with Tuples:

  ```py
  # Data to be inserted as a list of tuples
  data = [
    ("Alice", 35000),
    ("Bob", 40000),
    ("Charlie", 45000)]

  # Insert data using executemany()
  cursor.executemany("INSERT INTO employees (name, salary) VALUES (?, ?)", data)

  # Commit the changes and close the connection
  conn.commit()
  ```  
- Querying Data:
  
  ```py
  cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    for row in data:
        print(row)

  ```
- Updating Data:
  
  ```py
  cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (60000, "John Doe"))
  conn.commit()
  ```
- Deleting Data:
  
  ```py
  cursor.execute("DELETE FROM employees WHERE name = ?", ("John Doe",))
  conn.commit()
  ```
