import os
import mysql.connector
from mysql.connector import Error
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self, db_config):
        """Initialize the database connection."""
        self.db_config = db_config
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(**self.db_config)
                logger.info(f"Connected to database: {self.db_config.get('database')}")
            except Error as e:
                logger.error(f"Error connecting to database {self.db_config.get('database')}: {e}")
                self.connection = None
        return self.connection

    def close(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info(f"Closed connection to database: {self.db_config.get('database')}")

# Database configurations
DATABASES = {
    "testdb": {
        "host": os.getenv("DB_HOST", "db"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "database": os.getenv("DB_NAME_TESTDB", "testdb"),
        "user": os.getenv("DB_USER_TESTDB", "testuser"),
        "password": os.getenv("DB_PASSWORD_TESTDB", "testpassword"),
    },
    "mydatabase": {
        "host": os.getenv("DB_HOST", "db"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "database": os.getenv("DB_NAME_MYDATABASEW3", "mydatabase"),
        "user": os.getenv("DB_USER_MYDATABASEW3", "testuser"),
        "password": os.getenv("DB_PASSWORD_MYDATABASEW3", "testpassword"),
    },
}

# Initialize connections
testdb_conn = DatabaseConnection(DATABASES["testdb"])
mydatabase_conn = DatabaseConnection(DATABASES["mydatabase"])

if __name__ == "__main__":
    # Example usage
    conn1 = testdb_conn.connect()
    conn2 = mydatabase_conn.connect()

    # Close connections
    testdb_conn.close()
    mydatabase_conn.close()
