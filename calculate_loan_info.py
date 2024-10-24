
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_loan_info(p_customer_id):
    connection = engine.connect()
    try:
        query = text("""
            SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), 
                   COALESCE(ROUND(SUM(repayment_amount), 2), 0), 
                   COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
            FROM loans
            WHERE loans.customer_id = :p_customer_id
        """)
        result = connection.execute(query, {'p_customer_id': p_customer_id})
        row = result.fetchone()
        total_loan_amount, total_repayment, outstanding_loan_balance = row
        connection.commit()
        return total_loan_amount, total_repayment, outstanding_loan_balance
    finally:
        connection.close()

result = calculate_loan_info(123)
print(result)  # (total_loan_amount, total_repayment, outstanding_loan_balance)
