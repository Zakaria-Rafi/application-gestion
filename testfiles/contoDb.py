
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="selection_db"
    )
    print("Connected to MySQL!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
