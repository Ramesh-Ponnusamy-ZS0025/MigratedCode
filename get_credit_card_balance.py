
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id):
    # Create a connection object
    connection = engine.connect()

    # Define the SQL query
    query = text("""
        SELECT COALESCE(ROUND(SUM(balance), 2), 0) AS credit_card_balance
        FROM credit_cards
        WHERE credit_cards.customer_id = :p_customer_id
    """)

    # Execute the query with parameter
    result = connection.execute(query, {'p_customer_id': p_customer_id})

    # Fetch the result
    credit_card_balance = result.scalar()

    # Commit the changes (not necessary in this case, but included for completeness)
    connection.commit()

    # Close the connection
    connection.close()

    # Return the result
    return credit_card_balance
