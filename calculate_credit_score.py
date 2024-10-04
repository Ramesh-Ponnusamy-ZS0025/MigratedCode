
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    connection = engine.connect()

    # Call the procedures to get necessary data
    total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(p_customer_id, connection)
    credit_card_balance = get_credit_card_balance(p_customer_id, connection)
    late_pay_count = count_late_payments(p_customer_id, connection)
    v_credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

    # Update the customer's credit score
    update_query = text("UPDATE customers SET credit_score = :credit_score WHERE id = :customer_id")
    connection.execute(update_query, {'credit_score': round(v_credit_score, 0), 'customer_id': p_customer_id})
    connection.commit()

    # Optionally log very low scores
    if v_credit_score < 500:
        insert_query = text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:customer_id, :credit_score, NOW())")
        connection.execute(insert_query, {'customer_id': p_customer_id, 'credit_score': round(v_credit_score, 0)})
        connection.commit()

    connection.close()
    return round(v_credit_score, 0)


def calculate_loan_info(p_customer_id, connection):
    query = text("SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), COALESCE(ROUND(SUM(repayment_amount), 2), 0), COALESCE(ROUND(SUM(outstanding_balance), 2), 0) FROM loans WHERE customer_id = :customer_id")
    result = connection.execute(query, {'customer_id': p_customer_id})
    return result.fetchone()


def get_credit_card_balance(p_customer_id, connection):
    query = text("SELECT COALESCE(ROUND(SUM(balance), 2), 0) FROM credit_cards WHERE customer_id = :customer_id")
    result = connection.execute(query, {'customer_id': p_customer_id})
    return result.fetchone()[0]


def count_late_payments(p_customer_id, connection):
    query = text("SELECT COUNT(*) FROM payments WHERE customer_id = :customer_id AND status = 'Late'")
    result = connection.execute(query, {'customer_id': p_customer_id})
    return result.fetchone()[0]


def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    credit_score = 0

    if total_loan_amount > 0:
        credit_score += round((total_repayment / total_loan_amount) * 400, 2)
    else:
        credit_score += 400

    if credit_card_balance > 0:
        credit_score += round((1 - (credit_card_balance / 10000)) * 300, 2)
    else:
        credit_score += 300

    credit_score -= (late_pay_count * 50)

    if credit_score < 300:
        credit_score = 300
    elif credit_score > 850:
        credit_score = 850

    return credit_score
