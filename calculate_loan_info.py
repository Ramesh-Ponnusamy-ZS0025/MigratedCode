
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_loan_info(p_customer_id):
    connection = engine.connect()
    query = text("""
        SELECT 
            COALESCE(ROUND(SUM(loan_amount), 2), 0) AS total_loan_amount, 
            COALESCE(ROUND(SUM(repayment_amount), 2), 0) AS total_repayment, 
            COALESCE(ROUND(SUM(outstanding_balance), 2), 0) AS outstanding_loan_balance
        FROM loans
        WHERE loans.customer_id = :p_customer_id
    """)
    result = connection.execute(query, {"p_customer_id": p_customer_id})
    row = result.fetchone()
    connection.close()
    return row
