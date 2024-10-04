
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    connection = engine.connect()
    transaction = connection.begin()

    try:
        # Initialize credit score
        credit_score = 0

        # Calculate credit score
        if total_loan_amount > 0:
            query = text("SELECT ROUND((:total_repayment / :total_loan_amount) * 400, 2)")
            result = connection.execute(query, {'total_repayment': total_repayment, 'total_loan_amount': total_loan_amount})
            credit_score += result.scalar()
        else:
            credit_score += 400

        if credit_card_balance > 0:
            query = text("SELECT ROUND((1 - (:credit_card_balance / 10000)) * 300, 2)")
            result = connection.execute(query, {'credit_card_balance': credit_card_balance})
            credit_score += result.scalar()
        else:
            credit_score += 300

        credit_score -= (late_pay_count * 50)

        # Ensure credit score is within range
        if credit_score < 300:
            credit_score = 300
        elif credit_score > 850:
            credit_score = 850

        transaction.commit()
        return credit_score
    except Exception as e:
        transaction.rollback()
        raise e
    finally:
        connection.close()
