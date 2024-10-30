import psycopg2
from datetime import date

# Function to connect to the database; establishes and returns a connection to the PostgreSQL database.
def connect_db():
    try:
        # Connect to postgres; Stores the connection object if the connection is successful
        conn = psycopg2.connect("dbname=HRC_test user=postgres password=Qsoft1234")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")

# Establishing the connection; Stores the connection to the database by calling connect_db(). It connects to the HRC_test database.
connection = connect_db()

def delete_record(batch_id):
    """Delete a record from the hrc_input table."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM hrc_input WHERE batch_id = %s", (batch_id,))
        conn.commit()  # Commit the transaction
        print("Record deleted successfully.")
    except Exception as e:
        print(f"Error deleting record: {e}")
    finally:
        cursor.close()
        conn.close()

# Example; to test functionality
delete_record("J812")  # Delete record with batch_id="J812"