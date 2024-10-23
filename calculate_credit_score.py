
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    connection = engine.connect()

    # Call the procedures to get necessary data
    total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(p_customer_id)
    credit_card_balance = get_credit_card_balance(p_customer_id)
    late_pay_count = count_late_payments(p_customer_id)
    credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

    # Update the customer's credit score
    update_query = text("UPDATE customers SET credit_score = :credit_score WHERE id = :customer_id")
    connection.execute(update_query, {'credit_score': round(credit_score, 0), 'customer_id': p_customer_id})
    connection.commit()

    # Optionally log very low scores
    if credit_score < 500:
        insert_query = text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:customer_id, :credit_score, NOW())")
        connection.execute(insert_query, {'customer_id': p_customer_id, 'credit_score': round(credit_score, 0)})
        connection.commit()

    connection.close()

    return credit_score
