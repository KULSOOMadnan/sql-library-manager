import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Learning14",  # Replace with your MySQL root password
        database="library_db"
    )
    return conn
