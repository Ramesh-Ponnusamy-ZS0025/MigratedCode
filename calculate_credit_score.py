
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    conn = engine.connect()

    # Call the nested procedures to get necessary data
    total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(conn, p_customer_id)
    credit_card_balance = get_credit_card_balance(conn, p_customer_id)
    late_pay_count = count_late_payments(conn, p_customer_id)
    v_credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

    # Update the customer's credit score
    update_query = text("""
        UPDATE customers
        SET credit_score = ROUND(:credit_score, 0)
        WHERE customers.id = :customer_id
    """)
    conn.execute(update_query, {'credit_score': v_credit_score, 'customer_id': p_customer_id})

    # Optionally log very low scores
    if v_credit_score < 500:
        insert_query = text("""
            INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
            VALUES (:customer_id, ROUND(:credit_score, 0), NOW())
        """)
        conn.execute(insert_query, {'customer_id': p_customer_id, 'credit_score': v_credit_score})

    conn.commit()
    return v_credit_score


def calculate_loan_info(conn, p_customer_id):
    query = text("""
        SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0),
               COALESCE(ROUND(SUM(repayment_amount), 2), 0),
               COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
        FROM loans
        WHERE loans.customer_id = :customer_id
    """)
    result = conn.execute(query, {'customer_id': p_customer_id})
    total_loan_amount, total_repayment, outstanding_loan_balance = result.fetchone()
    return total_loan_amount, total_repayment, outstanding_loan_balance


def get_credit_card_balance(conn, p_customer_id):
    query = text("""
        SELECT COALESCE(ROUND(SUM(balance), 2), 0)
        FROM credit_cards
        WHERE credit_cards.customer_id = :customer_id
    """)
    result = conn.execute(query, {'customer_id': p_customer_id})
    credit_card_balance, = result.fetchone()
    return credit_card_balance


def count_late_payments(conn, p_customer_id):
    query = text("""
        SELECT COUNT(*)
        FROM payments
        WHERE payments.customer_id = :customer_id AND status = 'Late'
    """)
    result = conn.execute(query, {'customer_id': p_customer_id})
    late_pay_count, = result.fetchone()
    return late_pay_count


def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    credit_score = 0
    if total_loan_amount > 0:
        credit_score += ROUND((total_repayment / total_loan_amount) * 400, 2)
    else:
        credit_score += 400
    if credit_card_balance > 0:
        credit_score += ROUND((1 - (credit_card_balance / 10000)) * 300, 2)
    else:
        credit_score += 300
    credit_score -= (late_pay_count * 50)
    if credit_score < 300:
        credit_score = 300
    elif credit_score > 850:
        credit_score = 850
    return credit_score
