
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def count_late_payments(p_customer_id):
    # Create a connection object
    conn = engine.connect()

    # Define the SQL query
    query = text("""
        SELECT COUNT(*)
        FROM payments
        WHERE customer_id = :customer_id AND status = 'Late'
    """)

    # Execute the query with parameter binding
    result = conn.execute(query, {'customer_id': p_customer_id})

    # Fetch the result
    late_pay_count = result.scalar()

    # Commit the transaction (not necessary in this case, but included for completeness)
    conn.commit()

    # Close the connection
    conn.close()

    # Return the result
    return late_pay_count
