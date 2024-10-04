
from config import engine
import sqlalchemy as sa
import pandas as pd
import psycopg2

def get_late_pay_count(p_customer_id):
    # Create a connection object
    conn = engine.connect()

    # Define the SQL query as a text object
    query = sa.text("""
        SELECT COUNT(*)
        FROM payments
        WHERE payments.customer_id = :customer_id AND status = 'Late'
    """)

    try:
        # Execute the query with the customer_id parameter
        result = conn.execute(query, {'customer_id': p_customer_id})

        # Fetch the result
        late_pay_count = result.scalar()

        # Commit the changes (not necessary in this case, but included for completeness)
        conn.commit()

        # Return the result
        return late_pay_count

    except psycopg2.Error as e:
        # Handle any errors
        print(f"Error: {e}")
        return None

    finally:
        # Close the connection
        conn.close()
