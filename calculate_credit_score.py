
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    connection = engine.connect()
    try:
        # Call the procedures to get necessary data
        result = connection.execute(text("SELECT calculate_loan_info(:p_customer_id, :total_loan_amount, :total_repayment, :outstanding_loan_balance)"),
                                     {'p_customer_id': p_customer_id, 'total_loan_amount': 0, 'total_repayment': 0, 'outstanding_loan_balance': 0})
        total_loan_amount, total_repayment, outstanding_loan_balance = result.fetchone()

        result = connection.execute(text("SELECT get_credit_card_balance(:p_customer_id)"),
                                     {'p_customer_id': p_customer_id})
        credit_card_balance, = result.fetchone()

        from late_payments import count_late_payments  # Import the nested procedure
        late_pay_count = count_late_payments(p_customer_id)

        from credit_score_value import calculate_credit_score_value  # Import the nested procedure
        v_credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

        # Update the customer's credit score
        connection.execute(text("UPDATE customers SET credit_score = :credit_score WHERE id = :p_customer_id"),
                            {'credit_score': int(round(v_credit_score, 0)), 'p_customer_id': p_customer_id})
        connection.commit()

        # Optionally log very low scores
        if v_credit_score < 500:
            connection.execute(text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:p_customer_id, :credit_score, NOW())"),
                                {'p_customer_id': p_customer_id, 'credit_score': int(round(v_credit_score, 0))})
            connection.commit()

        return v_credit_score

    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
