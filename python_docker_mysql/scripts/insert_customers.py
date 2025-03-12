import logging
from connections import mydatabase_conn

# SQL to create table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255)
);
"""

# Insert query
insert_customers_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
customers_records = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

def execute_query(query, data=None, many=False):
    """Execute a SQL query with optional data."""
    try:
        connection = mydatabase_conn.connect()
        if connection is None:
            raise Exception("Failed to connect to the database.")

        with connection.cursor() as cursor:
            if data:
                if many:
                    cursor.executemany(query, data)
                else:
                    cursor.execute(query, data)
            else:
                cursor.execute(query)
            connection.commit()

        logging.info("Query executed successfully.")
    except Exception as e:
        logging.error(f"Error executing query: {e}")
    finally:
        mydatabase_conn.close()

# Create table if not exists
execute_query(create_table_query)

# Insert data
execute_query(insert_customers_query, customers_records, many=True)
