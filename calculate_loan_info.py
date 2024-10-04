
from config import engine
import sqlalchemy as sa
import pandas as pd
import psycopg2

def calculate_loan_info(p_customer_id):
    with engine.connect() as conn:
        query = sa.text("""
            SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), 
                   COALESCE(ROUND(SUM(repayment_amount), 2), 0), 
                   COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
            FROM loans
            WHERE loans.customer_id = :p_customer_id
        """)
        result = conn.execute(query, {'p_customer_id': p_customer_id})
        total_loan_amount, total_repayment, outstanding_loan_balance = result.fetchone()
        conn.commit()
    
    return total_loan_amount, total_repayment, outstanding_loan_balance
