import psycopg2
from datetime import date

# Function to connect to the database; establishes and returns a connection to the PostgreSQL database.
def connect_db():
    try:
        # Connect to HRC_test database; Stores the connection object if the connection is successful
        conn = psycopg2.connect("dbname=HRC_test user=postgres password=Qsoft1234")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")

def read_records():
    """Fetch all records from the hrc_input table."""
    try:
        conn = connect_db() # Establishing the connection; Stores the connection to the database by calling connect_db(). It connects to the HRC_test database.
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hrc_input")
        records = cursor.fetchall()  # Fetch all results
        for record in records:
            print(record)  # Print each record
    except Exception as e:
        print(f"Error reading records: {e}")
    finally:
        cursor.close()
        conn.close()

# Example; to test functionality
read_records()  # Read all records