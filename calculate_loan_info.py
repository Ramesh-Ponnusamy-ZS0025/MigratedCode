
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_loan_info(p_customer_id):
    connection = engine.connect()
    query = text(
        """
        SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), 
               COALESCE(ROUND(SUM(repayment_amount), 2), 0), 
               COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
        FROM loans
        WHERE loans.customer_id = :customer_id
        """
    )
    result = connection.execute(query, {"customer_id": p_customer_id})
    row = result.fetchone()
    connection.close()
    return {
        "total_loan_amount": row[0],
        "total_repayment": row[1],
        "outstanding_loan_balance": row[2]
    }
