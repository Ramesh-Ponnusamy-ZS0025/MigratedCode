
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    conn = engine.connect()

    try:
        # Initialize credit score
        credit_score = 0

        # Query to calculate credit score
        query = text("""
            SELECT 
                CASE 
                    WHEN :total_loan_amount > 0 THEN 
                        :credit_score + ROUND((:total_repayment / :total_loan_amount) * 400, 2)
                    ELSE 
                        :credit_score + 400
                END AS credit_score
        """)
        result = conn.execute(query, {
            "total_loan_amount": total_loan_amount,
            "credit_score": credit_score,
            "total_repayment": total_repayment
        })
        credit_score = result.fetchone()[0]

        # Update credit score based on credit card balance
        query = text("""
            SELECT 
                CASE 
                    WHEN :credit_card_balance > 0 THEN 
                        :credit_score + ROUND((1 - (:credit_card_balance / 10000)) * 300, 2)
                    ELSE 
                        :credit_score + 300
                END AS credit_score
        """)
        result = conn.execute(query, {
            "credit_card_balance": credit_card_balance,
            "credit_score": credit_score
        })
        credit_score = result.fetchone()[0]

        # Update credit score based on late payments
        credit_score -= late_pay_count * 50

        # Ensure credit score is within range
        if credit_score < 300:
            credit_score = 300
        elif credit_score > 850:
            credit_score = 850

        return credit_score

    finally:
        conn.close()
