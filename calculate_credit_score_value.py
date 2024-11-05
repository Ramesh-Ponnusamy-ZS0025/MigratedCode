
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    credit_score = 0

    with engine.connect() as connection:
        if total_loan_amount > 0:
            credit_score += connection.execute(text("SELECT ROUND((:repayment / :loan_amount) * 400, 2)"), {"repayment": total_repayment, "loan_amount": total_loan_amount}).scalar()
        else:
            credit_score += 400

        if credit_card_balance > 0:
            credit_score += connection.execute(text("SELECT ROUND((1 - (:balance / 10000)) * 300, 2)"), {"balance": credit_card_balance}).scalar()
        else:
            credit_score += 300

        credit_score -= late_pay_count * 50

        if credit_score < 300:
            credit_score = 300
        elif credit_score > 850:
            credit_score = 850

    return credit_score
