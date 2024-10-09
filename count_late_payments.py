
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def count_late_payments(p_customer_id):
    conn = engine.connect()
    try:
        query = text("SELECT COUNT(*) FROM payments WHERE customer_id = :customer_id AND status = 'Late'")
        result = conn.execute(query, {'customer_id': p_customer_id})
        late_pay_count = result.scalar()
        conn.commit()
        return late_pay_count
    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()
