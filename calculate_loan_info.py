
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_loan_info(customer_id):
    conn = engine.connect()
    try:
        query = text("""
            SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0) AS total_loan_amount,
                   COALESCE(ROUND(SUM(repayment_amount), 2), 0) AS total_repayment,
                   COALESCE(ROUND(SUM(outstanding_balance), 2), 0) AS outstanding_loan_balance
            FROM loans
            WHERE loans.customer_id = :customer_id
        """)
        result = conn.execute(query, {'customer_id': customer_id})
        row = result.fetchone()
        total_loan_amount, total_repayment, outstanding_loan_balance = row
        return total_loan_amount, total_repayment, outstanding_loan_balance
    finally:
        conn.close()

# Example usage:
customer_id = 123
total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
print(f"Total Loan Amount: {total_loan_amount}, Total Repayment: {total_repayment}, Outstanding Loan Balance: {outstanding_loan_balance}")
