
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    conn = engine.connect()

    try:
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(conn, p_customer_id)
        credit_card_balance = get_credit_card_balance(conn, p_customer_id)
        late_pay_count = count_late_payments(conn, p_customer_id)
        v_credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

        update_customer_credit_score = text("""
            UPDATE customers
            SET credit_score = ROUND(:v_credit_score, 0)
            WHERE customers.id = :p_customer_id
        """).bindparams(v_credit_score=v_credit_score, p_customer_id=p_customer_id)
        conn.execute(update_customer_credit_score)

        if v_credit_score < 500:
            insert_alert = text("""
                INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
                VALUES (:p_customer_id, ROUND(:v_credit_score, 0), NOW())
            """).bindparams(p_customer_id=p_customer_id, v_credit_score=v_credit_score)
            conn.execute(insert_alert)

        conn.commit()

        return v_credit_score

    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()


def calculate_loan_info(conn, p_customer_id):
    query = text("""
        SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0),
               COALESCE(ROUND(SUM(repayment_amount), 2), 0),
               COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
        FROM loans
        WHERE loans.customer_id = :p_customer_id
    """).bindparams(p_customer_id=p_customer_id)
    result = conn.execute(query)
    row = result.fetchone()
    return row[0], row[1], row[2]


def get_credit_card_balance(conn, p_customer_id):
    query = text("""
        SELECT COALESCE(ROUND(SUM(balance), 2), 0)
        FROM credit_cards
        WHERE credit_cards.customer_id = :p_customer_id
    """).bindparams(p_customer_id=p_customer_id)
    result = conn.execute(query)
    return result.fetchone()[0]


def count_late_payments(conn, p_customer_id):
    query = text("""
        SELECT COUNT(*)
        FROM payments
        WHERE payments.customer_id = :p_customer_id AND status = 'Late'
    """).bindparams(p_customer_id=p_customer_id)
    result = conn.execute(query)
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

    credit_score -= late_pay_count * 50

    if credit_score < 300:
        credit_score = 300
    elif credit_score > 850:
        credit_score = 850

    return credit_score
