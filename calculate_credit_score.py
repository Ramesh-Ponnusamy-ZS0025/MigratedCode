
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

from calculate_loan_info import calculate_loan_info
from get_credit_card_balance import get_credit_card_balance
from count_late_payments import count_late_payments
from calculate_credit_score_value import calculate_credit_score_value

def calculate_credit_score(p_customer_id):
    connection = engine.connect()
    
    try:
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(p_customer_id)
        credit_card_balance = get_credit_card_balance(p_customer_id)
        late_pay_count = count_late_payments(p_customer_id)
        credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        
        update_query = text("""
            UPDATE customers
            SET credit_score = :credit_score
            WHERE id = :p_customer_id
        """)
        connection.execute(update_query, {'credit_score': round(credit_score, 0), 'p_customer_id': p_customer_id})
        
        if credit_score < 500:
            insert_query = text("""
                INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
                VALUES (:p_customer_id, :credit_score, NOW())
            """)
            connection.execute(insert_query, {'p_customer_id': p_customer_id, 'credit_score': round(credit_score, 0)})
        
        connection.commit()
        
        return credit_score
    
    except psycopg2.Error as e:
        print(f"Error: {e}")
        connection.rollback()
    
    finally:
        connection.close()
