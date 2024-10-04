
from config import engine
import sqlalchemy as sa
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id: int) -> float:
    """
    Retrieve the credit card balance for a given customer ID.

    :param p_customer_id: Customer ID
    :return: Credit card balance
    """
    conn = engine.connect()
    try:
        query = sa.text("""
            SELECT COALESCE(ROUND(SUM(balance), 2), 0)
            FROM credit_cards
            WHERE credit_cards.customer_id = :p_customer_id
        """)
        result = conn.execute(query, {'p_customer_id': p_customer_id})
        credit_card_balance = result.scalar()
        conn.commit()
        return credit_card_balance
    finally:
        conn.close()
