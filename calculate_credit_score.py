
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    connection = engine.connect()
    transaction = connection.begin()

    try:
        # Call the procedures to get necessary data
        total_loan_amount, total_repayment, outstanding_loan_balance = connection.execute(text("SELECT * FROM calculate_loan_info(:p_customer_id)"), {'p_customer_id': p_customer_id}).fetchone()
        credit_card_balance, = connection.execute(text("SELECT * FROM get_credit_card_balance(:p_customer_id)"), {'p_customer_id': p_customer_id}).fetchone()
        late_pay_count, = connection.execute(text("SELECT * FROM count_late_payments(:p_customer_id)"), {'p_customer_id': p_customer_id}).fetchone()
        v_credit_score, = connection.execute(text("SELECT * FROM calculate_credit_score_value(:total_loan_amount, :total_repayment, :credit_card_balance, :late_pay_count)"),
                                               {'total_loan_amount': total_loan_amount, 'total_repayment': total_repayment, 
                                                'credit_card_balance': credit_card_balance, 'late_pay_count': late_pay_count}).fetchone()

        # Update the customer's credit score
        connection.execute(text("UPDATE customers SET credit_score = :credit_score WHERE id = :p_customer_id"),
                            {'credit_score': round(v_credit_score, 0), 'p_customer_id': p_customer_id})

        # Optionally log very low scores
        if v_credit_score < 500:
            connection.execute(text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:p_customer_id, :credit_score, NOW())"),
                               {'p_customer_id': p_customer_id, 'credit_score': round(v_credit_score, 0)})

        transaction.commit()
        return round(v_credit_score, 0)
    except Exception as e:
        transaction.rollback()
        raise e
    finally:
        connection.close()
