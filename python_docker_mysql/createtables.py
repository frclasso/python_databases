import os
import mysql.connector
from mysql.connector import Error
from conectiondb import conn


create_movies_table_query = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
create_reviewers_table_query = """
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""


create_ratings_table_query = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""


def createTable(query):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
        conn.close()
    except Exception as e:
        print(e)


createTable(query=create_movies_table_query)
createTable(query=create_reviewers_table_query)
createTable(query=create_ratings_table_query)


