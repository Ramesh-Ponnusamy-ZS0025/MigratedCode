
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id):
    # Create a connection object
    conn = engine.connect()

    # Define the SQL query as a text object
    query = text("""
        SELECT COALESCE(ROUND(SUM(balance), 2), 0) AS credit_card_balance
        FROM credit_cards
        WHERE credit_cards.customer_id = :p_customer_id
    """)

    # Execute the query with the parameter
    result = conn.execute(query, {"p_customer_id": p_customer_id})

    # Fetch the result
    credit_card_balance = result.fetchone()[0]

    # Commit the changes (not necessary in this case, but good practice)
    conn.commit()

    # Close the connection
    conn.close()

    # Return the result
    return credit_card_balance
