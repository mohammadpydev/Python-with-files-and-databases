import mysql.connector

class UserDatabase:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                email VARCHAR(255)
            )
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_user(self, username, email):
        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        user_data = (username, email)
        self.cursor.execute(insert_query, user_data)
        self.conn.commit()

    def print_all_users(self):
        select_query = "SELECT * FROM users"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def update_user_email(self, username, new_email):
        update_query = "UPDATE users SET email = %s WHERE username = %s"
        update_data = (new_email, username)
        self.cursor.execute(update_query, update_data)
        self.conn.commit()

    def delete_user(self, username):
        delete_query = "DELETE FROM users WHERE username = %s"
        self.cursor.execute(delete_query, (username,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Example usage:
db = UserDatabase('your_host', 'your_username', 'your_password', 'your_database')
db.create_table()
db.insert_user('john_doe', 'john@example.com')
db.insert_user('jane_smith', 'jane@example.com')
db.print_all_users()
db.update_user_email('john_doe', 'new_email@example.com')
db.delete_user('jane_smith')
db.print_all_users()
db.close_connection()