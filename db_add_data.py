import psycopg2
from datetime import date

# Function to connect to the database; establishes and returns a connection to the PostgreSQL database.
def connect_db():
    try:
        # Connect to postgres; stores the connection object if the connection is successful
        conn = psycopg2.connect("dbname=HRC_test user=postgres password=Qsoft1234")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")

# Establishing the connection; stores the connection to the database by calling connect_db(). It connects to the HRC_test database.
connection = connect_db()

#Function to add record data
def add_record(records):
    """Insert a new data record into the hrc_Input table."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT INTO hrc_input (date, issued_by, batch_id, vessel, qty_coil, tonnage, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (records)
        )
        conn.commit()  # Commit the transaction
        print("Records created successfully.")
    except Exception as e:
        print(f"Error creating record: {e}")
    finally:
        cursor.close()
        conn.close()

# Example; to test functionality
add_record([(date.today(), "Alis", "J813", "Pulau Taoyi", 10, 100, "Draft"),
            (date.today(), "Alis", "J814", "Kalapati", 20, 200, "Draft"),
            (date.today(), "Alis", "J815", "Pulau Taoyi", 30, 30, "Draft"),
            (date.today(), "Alis", "J816", "Tropical Venus", 70, 150, "Draft"),
            (date.today(), "Alis", "J817", "Tropical Venus", 15, 120, "Draft")])  # Create 5 new record