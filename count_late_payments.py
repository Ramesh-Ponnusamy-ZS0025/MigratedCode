
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def count_late_payments(p_customer_id):
    conn = engine.connect()
    query = text("SELECT COUNT(*) FROM payments WHERE payments.customer_id = :customer_id AND status = 'Late'")
    result = conn.execute(query, {'customer_id': p_customer_id})
    late_pay_count = result.scalar()
    conn.close()
    return late_pay_count
