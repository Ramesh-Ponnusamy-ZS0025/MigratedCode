
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    connection = engine.connect()
    transaction = connection.begin()

    try:
        sql = text("""
            SELECT 
                CASE 
                    WHEN :total_loan_amount > 0 THEN 
                        400 + ROUND((:total_repayment / :total_loan_amount) * 400, 2)
                    ELSE 
                        800
                END +
                CASE 
                    WHEN :credit_card_balance > 0 THEN 
                        ROUND((1 - (:credit_card_balance / 10000)) * 300, 2)
                    ELSE 
                        300
                END -
                (:late_pay_count * 50) 
                AS credit_score
        """)

        result = connection.execute(sql, {
            'total_loan_amount': total_loan_amount,
            'total_repayment': total_repayment,
            'credit_card_balance': credit_card_balance,
            'late_pay_count': late_pay_count
        }).fetchone()

        credit_score = max(300, min(850, result[0]))

        transaction.commit()
        connection.close()

        return credit_score
    except psycopg2.Error as e:
        transaction.rollback()
        connection.close()
        raise e
