import os
import mysql.connector 
from mysql.connector import Error
import logging
from conectiondb import conn

select_movies_inner_join_ratings_query = """
                        SELECT title, AVG(rating) as average_rating
                        FROM ratings
                        INNER JOIN movies
                        ON movies.id = ratings.movie_id
                        GROUP BY movie_id
                        ORDER BY average_rating DESC
                        LIMIT 5
                    """

def joinAndSelectTables(query):
    try:
        # conn = mysql.connector.connect(**db_config)
        with conn.cursor() as cursor:
            cursor.execute(query)
            for movie in cursor.fetchall():
                print(movie)
        return logging.info(f"Query executed succesfully.")
    except Exception as e:
        print(e)

joinAndSelectTables(query=select_movies_inner_join_ratings_query)
print()

# ('The Godfather', Decimal('9.90000'))
# ('Night of the Living Dead', Decimal('9.90000'))
# ('Avengers: Endgame', Decimal('9.75000'))
# ('Eternal Sunshine of the Spotless Mind', Decimal('8.90000'))
# ('Beasts of No Nation', Decimal('8.70000'))


select_movies_query = """
                        SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
                        FROM reviewers
                        INNER JOIN ratings
                        ON reviewers.id = ratings.reviewer_id
                        GROUP BY reviewer_id
                        ORDER BY num DESC
                        LIMIT 1
                    """

joinAndSelectTables(query=select_movies_query)
#('Mary Cooper', 4)