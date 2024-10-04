
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id):
    with engine.connect() as conn:
        query = text("""
            SELECT COALESCE(ROUND(SUM(balance), 2), 0)
            FROM credit_cards
            WHERE credit_cards.customer_id = :p_customer_id
        """)
        result = conn.execute(query, {"p_customer_id": p_customer_id})
        credit_card_balance = result.scalar()
        conn.commit()
    return credit_card_balance
