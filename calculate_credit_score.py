
from config import engine
import pandas as pd
from sqlalchemy import text
import psycopg2

def calculate_credit_score(p_customer_id):
    total_loan_amount = 0
    total_repayment = 0
    outstanding_loan_balance = 0
    credit_card_balance = 0
    late_pay_count = 0
    v_credit_score = 0

    with engine.connect() as connection:
        # Step 1: Calculate the customer's total loan amount, total repayment, and outstanding balance
        query = text("""
            SELECT COALESCE(ROUND(SUM(loan_amount), 2), 0), COALESCE(ROUND(SUM(repayment_amount), 2), 0), COALESCE(ROUND(SUM(outstanding_balance), 2), 0)
            FROM loans
            WHERE loans.customer_id = :customer_id
        """)
        result = connection.execute(query, {"customer_id": p_customer_id})
        total_loan_amount, total_repayment, outstanding_loan_balance = result.fetchone()

        # Step 2: Get the current credit card balance
        query = text("""
            SELECT COALESCE(ROUND(SUM(balance), 2), 0)
            FROM credit_cards
            WHERE credit_cards.customer_id = :customer_id
        """)
        result = connection.execute(query, {"customer_id": p_customer_id})
        credit_card_balance, = result.fetchone()

        # Step 3: Count the number of late payments
        query = text("""
            SELECT COUNT(*)
            FROM payments
            WHERE payments.customer_id = :customer_id AND status = 'Late'
        """)
        result = connection.execute(query, {"customer_id": p_customer_id})
        late_pay_count, = result.fetchone()

        # Step 4: Basic rule-based calculation of the credit score
        if total_loan_amount > 0:
            v_credit_score += round((total_repayment / total_loan_amount) * 400, 2)  # 40% weight for loan repayment
        else:
            v_credit_score += 400  # If no loans, give average score for this factor

        if credit_card_balance > 0:
            v_credit_score += round((1 - (credit_card_balance / 10000)) * 300, 2)  # 30% weight for credit card utilization
        else:
            v_credit_score += 300

        v_credit_score -= late_pay_count * 50  # Deduct 50 points for each late payment

        # Ensure the score stays within reasonable bounds (e.g., 300 to 850)
        if v_credit_score < 300:
            v_credit_score = 300
        elif v_credit_score > 850:
            v_credit_score = 850

        # Update the customer's credit score
        query = text("""
            UPDATE customers
            SET credit_score = ROUND(:credit_score, 0)
            WHERE customers.id = :customer_id
        """)
        connection.execute(query, {"credit_score": v_credit_score, "customer_id": p_customer_id})
        connection.commit()

        # Optionally, log the result or raise an alert for very low scores
        if v_credit_score < 500:
            query = text("""
                INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
                VALUES (:customer_id, ROUND(:credit_score, 0), NOW())
            """)
            connection.execute(query, {"customer_id": p_customer_id, "credit_score": v_credit_score})
            connection.commit()

    return v_credit_score