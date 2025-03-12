import mysql.connector
import os

# Use the correct host based on Docker environment
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST", "db"),  # Uses "db" as default
    user=os.getenv("DB_USER", "testuser"),
    password=os.getenv("DB_PASSWORD", "testpassword")
)

mycursor = mydb.cursor()

# Create the new database
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("Database 'mydatabase' created successfully!")

# Close the connection
mydb.close()
