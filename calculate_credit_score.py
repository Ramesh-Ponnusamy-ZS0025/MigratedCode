
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    conn = engine.connect()

    # Step 1: Calculate the customer's total loan amount, total repayment, and outstanding balance
    query = text("""
        SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), COALESCE(ROUND(SUM(repayment_amount), 2), 0), COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
        FROM loans
        WHERE loans.customer_id = :p_customer_id
    """)
    result = conn.execute(query, {"p_customer_id": p_customer_id}).fetchone()
    total_loan_amount, total_repayment, outstanding_loan_balance = result

    # Step 2: Get the current credit card balance
    query = text("""
        SELECT COALESCE(ROUND(SUM(balance), 2), 0)
        FROM credit_cards
        WHERE credit_cards.customer_id = :p_customer_id
    """)
    credit_card_balance = conn.execute(query, {"p_customer_id": p_customer_id}).scalar()

    # Step 3: Count the number of late payments
    query = text("""
        SELECT COUNT(*)
        FROM payments
        WHERE payments.customer_id = :p_customer_id AND status = 'Late'
    """)
    late_pay_count = conn.execute(query, {"p_customer_id": p_customer_id}).scalar()

    # Step 4: Basic rule-based calculation of the credit score
    v_credit_score = 0
    if total_loan_amount > 0:
        v_credit_score += round((total_repayment / total_loan_amount) * 400, 2)  # 40% weight for loan repayment
    else:
        v_credit_score += 400  # If no loans, give average score for this factor

    if credit_card_balance > 0:
        v_credit_score += round((1 - (credit_card_balance / 10000)) * 300, 2)  # 30% weight for credit card utilization
    else:
        v_credit_score += 300

    v_credit_score -= (late_pay_count * 50)  # Deduct 50 points for each late payment

    # Ensure the score stays within reasonable bounds (e.g., 300 to 850)
    if v_credit_score < 300:
        v_credit_score = 300
    elif v_credit_score > 850:
        v_credit_score = 850

    # Update the customer's credit score
    query = text("""
        UPDATE customers
        SET credit_score = :credit_score
        WHERE customers.id = :p_customer_id
    """)
    conn.execute(query, {"credit_score": round(v_credit_score, 0), "p_customer_id": p_customer_id})
    conn.commit()

    # Optionally, log the result or raise an alert for very low scores
    if v_credit_score < 500:
        query = text("""
            INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
            VALUES (:p_customer_id, :credit_score, NOW())
        """)
        conn.execute(query, {"p_customer_id": p_customer_id, "credit_score": round(v_credit_score, 0)})
        conn.commit()

    conn.close()
    return round(v_credit_score, 0)
