import os
import mysql.connector 
from mysql.connector import Error
import logging
from decimal import Decimal
from conectiondb import conn

select_movies_query = """
                        SELECT CONCAT(title, " (", release_year, ")"),
                            collection_in_mil
                        FROM movies
                        ORDER BY collection_in_mil DESC
                        LIMIT 5
                        """
with conn.cursor() as cursor:
     cursor.execute(select_movies_query)
     for movie in cursor.fetchall():
         print(movie)

# ('Avengers: Endgame (2019)', Decimal('858.8'))
# ('Titanic (1997)', Decimal('659.2'))
# ('The Dark Knight (2008)', Decimal('535.4'))
# ('Toy Story 4 (2019)', Decimal('434.9'))
# ('The Lion King (1994)', Decimal('423.6'))