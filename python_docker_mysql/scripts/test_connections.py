import os
import mysql.connector 
from mysql.connector import Error
import logging
from connections import mydatabase_conn , testdb_conn

conn = testdb_conn.connect()
cursor = conn.cursor()
cursor.execute("SELECT  COUNT(*) FROM movies")
results = cursor.fetchall()
print(results)
testdb_conn.close()

# print()
# conn = mydatabase_conn.connect()
# cursor = conn.cursor()
# cursor.execute("SELECT COUNT(*) FROM customers")
# results = cursor.fetchall()
# print(results)
# mydatabase_conn.close()
