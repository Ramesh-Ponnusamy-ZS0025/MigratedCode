
from config import engine
import sqlalchemy as sa
import pandas as pd
import psycopg2

def count_late_payments(p_customer_id: int) -> int:
    """
    Count late payments for a given customer ID
    """
    conn = engine.connect()
    try:
        query = sa.text("""
            SELECT COUNT(*)
            FROM payments
            WHERE customer_id = :customer_id AND status = 'Late'
        """)
        result = conn.execute(query, {'customer_id': p_customer_id})
        late_pay_count = result.scalar()
        conn.commit()
        return late_pay_count
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()
