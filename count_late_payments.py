
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def count_late_payments(p_customer_id):
    with engine.connect() as connection:
        query = text("SELECT COUNT(*) FROM payments WHERE customer_id = :customer_id AND status = 'Late'")
        result = connection.execute(query, {'customer_id': p_customer_id})
        late_pay_count = result.scalar()
    return late_pay_count
