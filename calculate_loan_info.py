
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_loan_info(customer_id: int) -> tuple:
    connection = engine.connect()
    try:
        query = text("""
            SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), 
                   COALESCE(ROUND(SUM(repayment_amount), 2), 0), 
                   COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
            FROM loans
            WHERE loans.customer_id = :customer_id
        """)
        result = connection.execute(query, {'customer_id': customer_id})
        row = result.fetchone()
        connection.close()
        return row
    except psycopg2.Error as e:
        connection.close()
        raise e
