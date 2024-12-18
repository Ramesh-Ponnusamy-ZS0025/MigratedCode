
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

# Nested procedure imports
from calculate_loan_info import calculate_loan_info
from get_credit_card_balance import get_credit_card_balance
from count_late_payments import count_late_payments
from calculate_credit_score_value import calculate_credit_score_value

def calculate_credit_score(p_customer_id):
    connection = engine.connect()

    # Call the procedures to get necessary data
    total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(p_customer_id)
    credit_card_balance = get_credit_card_balance(p_customer_id)
    late_pay_count = count_late_payments(p_customer_id)
    credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

    # Update the customer's credit score
    update_query = text("UPDATE customers SET credit_score = ROUND(:credit_score, 0) WHERE customers.id = :customer_id")
    result = connection.execute(update_query, {'credit_score': credit_score, 'customer_id': p_customer_id})
    connection.commit()

    # Optionally log very low scores
    if credit_score < 500:
        insert_query = text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:customer_id, ROUND(:credit_score, 0), NOW())")
        result = connection.execute(insert_query, {'customer_id': p_customer_id, 'credit_score': credit_score})
        connection.commit()

    connection.close()
    return credit_score
