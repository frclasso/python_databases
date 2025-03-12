import os
import mysql.connector 
from mysql.connector import Error
import logging
from decimal import Decimal
from python_docker_mysql.scripts.connection_testdb import conn

select_movies_query = """
                        SELECT title, collection_in_mil
                        FROM movies
                        WHERE collection_in_mil > 300
                        ORDER BY collection_in_mil DESC
                    """

with conn.cursor() as cursor:
     cursor.execute(select_movies_query)
     for movie in cursor.fetchall():
         print(movie)



# ('Avengers: Endgame', Decimal('858.8'))
# ('Titanic', Decimal('659.2'))
# ('The Dark Knight', Decimal('535.4'))
# ('Toy Story 4', Decimal('434.9'))
# ('The Lion King', Decimal('423.6'))
# ('Deadpool', Decimal('363.6'))
# ('Forrest Gump', Decimal('330.2'))
# ('Skyfall', Decimal('304.6'))