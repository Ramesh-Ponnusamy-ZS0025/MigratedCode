
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    connection = engine.connect()
    try:
        # Initialize credit_score
        credit_score = 0

        # Calculate credit_score
        if total_loan_amount > 0:
            credit_score += connection.execute(text("SELECT ROUND((:total_repayment / :total_loan_amount) * 400, 2)").bindparams(total_repayment=total_repayment, total_loan_amount=total_loan_amount)). scalar()
        else:
            credit_score += 400

        if credit_card_balance > 0:
            credit_score += connection.execute(text("SELECT ROUND((1 - (:credit_card_balance / 10000)) * 300, 2)").bindparams(credit_card_balance=credit_card_balance)).scalar()
        else:
            credit_score += 300

        credit_score -= late_pay_count * 50

        # Ensure credit_score is within range
        if credit_score < 300:
            credit_score = 300
        elif credit_score > 850:
            credit_score = 850

        return credit_score
    finally:
        connection.commit()
        connection.close()
