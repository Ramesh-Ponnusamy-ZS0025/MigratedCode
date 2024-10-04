
from config import engine  # import database connection configuration
import pandas as pd
from sqlalchemy import text

def get_loan_summary(customer_id):
    conn = engine.connect()  # create a connection object
    
    # define the SQL query with placeholders for parameters
    query = text("""
        SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), 
               COALESCE(ROUND(SUM(repayment_amount), 2), 0), 
               COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
        FROM loans
        WHERE loans.customer_id = :customer_id;
    """)
    
    # execute the query with parameter dictionary
    result = conn.execute(query, {'customer_id': customer_id})
    
    # fetch the results as a single row
    row = result.fetchone()
    
    # create a dictionary to store the results
    loan_summary = {
        'total_loan_amount': row[0],
        'total_repayment': row[1],
        'outstanding_loan_balance': row[2]
    }
    
    conn.close()  # close the connection
    
    return loan_summary
