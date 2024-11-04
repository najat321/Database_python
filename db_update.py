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

def update_record(new_issue_date, new_issued_by, new_batch_id, new_vessel, new_quantity, new_tonnage, new_status, batch_id):
    """Update an existing record in the hrc_input table."""
    try:
        conn = connect_db() # Establishing the connection; Stores the connection to the database by calling connect_db(). It connects to the HRC_test database.
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE hrc_input SET date = %s, issued_by = %s, batch_id = %s, vessel = %s, qty_coil = %s, tonnage = %s, status = %s WHERE batch_id = %s",
            (new_issue_date, new_issued_by, new_batch_id, new_vessel, new_quantity, new_tonnage, new_status, batch_id)
        )
        conn.commit()  # Commit the transaction; saves the new data in the database
        print("Record updated successfully.")
    except Exception as e:
        print(f"Error updating record: {e}")
    finally:
        cursor.close()
        conn.close()

# Example; to test functionality
update_record(date.today(), "Alis", "J812", "Kalapati", 8, 200, "Posted to Macola", "J813")  # Update record with batch_id="J813"