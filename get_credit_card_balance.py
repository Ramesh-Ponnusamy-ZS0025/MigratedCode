
from config import engine
import sqlalchemy as sa
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id):
    conn = engine.connect()
    try:
        query = text("""
            SELECT COALESCE(ROUND(SUM(balance), 2), 0)
            FROM credit_cards
            WHERE credit_cards.customer_id = :customer_id
        """)
        result = conn.execute(query, {'customer_id': p_customer_id})
        credit_card_balance = result.scalar()
        conn.commit()
        return credit_card_balance
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
