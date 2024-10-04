
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    connection = engine.connect()

    # Call the procedures to get necessary data
    result = connection.execute(text("SELECT calculate_loan_info(:p_customer_id, :total_loan_amount, :total_repayment, :outstanding_loan_balance)"),
                                {'p_customer_id': p_customer_id, 'total_loan_amount': None, 'total_repayment': None, 'outstanding_loan_balance': None})
    total_loan_amount, total_repayment, outstanding_loan_balance = result.fetchone()

    result = connection.execute(text("SELECT get_credit_card_balance(:p_customer_id, :credit_card_balance)"),
                                {'p_customer_id': p_customer_id, 'credit_card_balance': None})
    credit_card_balance, = result.fetchone()

    result = connection.execute(text("SELECT count_late_payments(:p_customer_id, :late_pay_count)"),
                                {'p_customer_id': p_customer_id, 'late_pay_count': None})
    late_pay_count, = result.fetchone()

    result = connection.execute(text("SELECT calculate_credit_score_value(:total_loan_amount, :total_repayment, :credit_card_balance, :late_pay_count, :v_credit_score)"),
                                {'total_loan_amount': total_loan_amount, 'total_repayment': total_repayment, 'credit_card_balance': credit_card_balance, 'late_pay_count': late_pay_count, 'v_credit_score': None})
    v_credit_score, = result.fetchone()

    # Update the customer's credit score
    connection.execute(text("UPDATE customers SET credit_score = :credit_score WHERE id = :p_customer_id"),
                        {'credit_score': round(v_credit_score, 0), 'p_customer_id': p_customer_id})
    connection.commit()

    # Optionally log very low scores
    if v_credit_score < 500:
        connection.execute(text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:p_customer_id, :credit_score, NOW())"),
                            {'p_customer_id': p_customer_id, 'credit_score': round(v_credit_score, 0)})
        connection.commit()

    connection.close()

    return round(v_credit_score, 0)
