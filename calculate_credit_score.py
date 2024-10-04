
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    connection = engine.connect()

    # Call the procedures to get necessary data
    total_loan_amount, total_repayment, outstanding_loan_balance = connection.execute(text("""
        SELECT * FROM calculate_loan_info(:p_customer_id)
    """), {"p_customer_id": p_customer_id}).fetchone()

    credit_card_balance = connection.execute(text("""
        SELECT * FROM get_credit_card_balance(:p_customer_id)
    """), {"p_customer_id": p_customer_id}).scalar()

    late_pay_count = connection.execute(text("""
        SELECT * FROM count_late_payments(:p_customer_id)
    """), {"p_customer_id": p_customer_id}).scalar()

    credit_score = connection.execute(text("""
        SELECT * FROM calculate_credit_score_value(:total_loan_amount, :total_repayment, :credit_card_balance, :late_pay_count)
    """), {"total_loan_amount": total_loan_amount, "total_repayment": total_repayment, "credit_card_balance": credit_card_balance, "late_pay_count": late_pay_count}).scalar()

    # Update the customer's credit score
    connection.execute(text("""
        UPDATE customers
        SET credit_score = ROUND(:credit_score, 0)
        WHERE customers.id = :p_customer_id
    """), {"credit_score": credit_score, "p_customer_id": p_customer_id})

    connection.commit()

    # Optionally log very low scores
    if credit_score < 500:
        connection.execute(text("""
            INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
            VALUES (:p_customer_id, ROUND(:credit_score, 0), NOW())
        """), {"p_customer_id": p_customer_id, "credit_score": credit_score})
        connection.commit()

    connection.close()

    return credit_score
