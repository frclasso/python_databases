import os
import mysql.connector 
from mysql.connector import Error
import logging

db_config = {
    "host": os.getenv("DB_HOST", "db"),
    "port": os.getenv("DB_PORT", 3306),
    "database": os.getenv("DB_NAME", "testdb"),
    "user": os.getenv("DB_USER", "testuser"),
    "password": os.getenv("DB_PASSWORD", "testpassword"),
}


conn = mysql.connector.connect(**db_config)