
from config import engine
import pandas as pd
from sqlalchemy import text
import psycopg2

def get_late_pay_count(p_customer_id):
    conn = engine.connect()
    try:
        query = text("""
            SELECT COUNT(*)
            FROM payments
            WHERE payments.customer_id = :customer_id AND status = 'Late'
        """)
        result = conn.execute(query, {'customer_id': p_customer_id})
        late_pay_count = result.scalar()
        conn.commit()
        return late_pay_count
    finally:
        conn.close()
