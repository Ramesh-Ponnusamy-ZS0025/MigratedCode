
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    with engine.connect() as connection:
        connection.execute(text("""
            SELECT 
                CASE 
                    WHEN :total_loan_amount > 0 THEN 
                        ROUND(:total_repayment / :total_loan_amount * 400, 2)
                    ELSE 
                        400 
                END 
                + 
                CASE 
                    WHEN :credit_card_balance > 0 THEN 
                        ROUND((1 - :credit_card_balance / 10000) * 300, 2)
                    ELSE 
                        300 
                END 
                - (:late_pay_count * 50) 
                AS credit_score
        """), {
            'total_loan_amount': total_loan_amount,
            'total_repayment': total_repayment,
            'credit_card_balance': credit_card_balance,
            'late_pay_count': late_pay_count
        })

        result = connection.execute(text("SELECT credit_score")).fetchone()

        credit_score = result[0]

        if credit_score < 300:
            credit_score = 300
        elif credit_score > 850:
            credit_score = 850

        return credit_score
