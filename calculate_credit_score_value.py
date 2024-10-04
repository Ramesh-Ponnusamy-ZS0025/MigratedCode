
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    conn = engine.connect()

    # Initialize credit score
    credit_score = 0

    # Calculate credit score based on loan amounts and repayment
    if total_loan_amount > 0:
        loan_query = text("""
            SELECT ROUND((:total_repayment / :total_loan_amount) * 400, 2) AS score
        """)
        result = conn.execute(loan_query, {'total_repayment': total_repayment, 'total_loan_amount': total_loan_amount})
        credit_score += result.scalar()

    else:
        credit_score += 400

    # Calculate credit score based on credit card balance
    if credit_card_balance > 0:
        credit_card_query = text("""
            SELECT ROUND((1 - (:credit_card_balance / 10000)) * 300, 2) AS score
        """)
        result = conn.execute(credit_card_query, {'credit_card_balance': credit_card_balance})
        credit_score += result.scalar()

    else:
        credit_score += 300

    # Deduct points for late payments
    credit_score -= late_pay_count * 50

    # Ensure credit score is within valid range
    if credit_score < 300:
        credit_score = 300
    elif credit_score > 850:
        credit_score = 850

    conn.close()
    return credit_score
