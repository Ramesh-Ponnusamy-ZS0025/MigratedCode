
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def get_credit_card_balance(p_customer_id):
    connection = engine.connect()
    try:
        query = text("SELECT COALESCE(ROUND(SUM(balance), 2), 0) FROM credit_cards WHERE customer_id = :customer_id")
        result = connection.execute(query, {"customer_id": p_customer_id})
        credit_card_balance = result.fetchone()[0]
        connection.commit()
        return credit_card_balance
    except psycopg2.Error as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        connection.close()
