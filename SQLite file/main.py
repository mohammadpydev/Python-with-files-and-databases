import sqlite3

class SQLiteHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Connected to {self.db_name}")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print(f"Disconnected from {self.db_name}")
        self.conn = None

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def fetch_all(self,table_name):
        self.cursor.execute(f"SELECT rowid, * FROM {table_name}")
        return self.cursor.fetchall()


    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close_cursor(self):
        self.cursor.close()

    def create_table(self, table_name, schema):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        self.execute(query)
        self.commit()

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in range(len(data))])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.execute(query, data)
        self.commit()

    def insert_many_data(db_name, table_name, data_list):
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            # Define the SQL INSERT statement with placeholders
            placeholders = ', '.join(['?' for _ in range(len(data_list[0]))])
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"

            # Use executemany() to insert multiple rows
            cursor.executemany(query, data_list)

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            print(f"Inserted {len(data_list)} rows into {table_name} in {db_name}")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")    

    def update_data(self, table_name, data, condition):
        query = f"UPDATE {table_name} SET {data} WHERE {condition}"
        self.execute(query)
        self.commit()

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute(query)
        self.commit()

    def select_data(self, table_name, columns='*', condition=None):
        if condition:
            query = f"SELECT {columns} FROM {table_name} WHERE {condition}"
        else:
            query = f"SELECT {columns} FROM {table_name}"
        self.execute(query)
        return self.fetch_all()

    def execute_script(self, script):
        try:
            self.conn.executescript(script)
            self.commit()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


db_handler = SQLiteHandler('mydatabase.db')
db_handler.connect()

# Create a table
table_schema = "name TEXT, salary REAL"
db_handler.create_table("employees", table_schema)

# Insert data
data = ("John Doe", 50000)
db_handler.insert_data("employees", data)

# or

db_name = 'mydatabase.db'
table_name = 'employees'

data_list = [
    ("Alice", 35000),
    ("Bob", 40000),
    ("Charlie", 45000),
]

db_handler.insert_many_data(db_name, table_name, data_list)

# Query data
result = db_handler.select_data("employees", "*", "name = 'John Doe'")
print(result)

db_handler.disconnect()
