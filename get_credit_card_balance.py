
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id):
    connection = engine.connect()
    query = text("""
        SELECT COALESCE(ROUND(SUM(balance), 2), 0)
        FROM credit_cards
        WHERE credit_cards.customer_id = :p_customer_id
    """)
    result = connection.execute(query, {"p_customer_id": p_customer_id})
    credit_card_balance = result.scalar()
    connection.close()
    return credit_card_balance
