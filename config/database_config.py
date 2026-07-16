import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establishes and returns a database connection pool pointer."""
    try:
        return mysql.connector.connect(
            host="YOUR_REMOTE_SERVER_IP",
            database="retrorealmgames",
            user="YOUR_USERNAME",
            password="YOUR_PASSWORD"
        )
    except Error as e:
        print(f"Secure database gateway link severed: {e}")
        return None
