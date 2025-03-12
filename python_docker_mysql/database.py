import os
import mysql.connector
from mysql.connector import Error
from conectiondb import conn

# # Load environment variables
# db_config = {
#     "host": os.getenv("DB_HOST", "db"),
#     "port": os.getenv("DB_PORT", 3306),
#     "database": os.getenv("DB_NAME", "testdb"),
#     "user": os.getenv("DB_USER", "testuser"),
#     "password": os.getenv("DB_PASSWORD", "testpassword"),
# }

# Connect to MySQL
try:
    # conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Connected to MySQL Database!")
    conn.close()
except Error as e:
    print(f"Error: {e}")



