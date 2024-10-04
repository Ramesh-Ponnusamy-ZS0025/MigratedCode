
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def count_late_payments(p_customer_id):
    connection = engine.connect()
    query = text("SELECT COUNT(*) FROM payments WHERE customer_id = :p_customer_id AND status = 'Late'")
    result = connection.execute(query, {'p_customer_id': p_customer_id})
    late_pay_count = result.scalar()
    connection.close()
    return late_pay_count

from another_file import calculate_loan_info
