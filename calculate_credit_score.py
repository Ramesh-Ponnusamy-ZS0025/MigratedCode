
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_credit_score(p_customer_id):
    with engine.connect() as connection:
        # Call the procedures to get necessary data
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(p_customer_id)
        credit_card_balance = get_credit_card_balance(p_customer_id)
        late_pay_count = count_late_payments(p_customer_id)
        credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)

        # Update the customer's credit score
        update_query = text("UPDATE customers SET credit_score = :credit_score WHERE id = :customer_id")
        connection.execute(update_query, {"credit_score": round(credit_score, 0), "customer_id": p_customer_id})
        connection.commit()

        # Optionally log very low scores
        if credit_score < 500:
            insert_query = text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:customer_id, :credit_score, NOW())")
            connection.execute(insert_query, {"customer_id": p_customer_id, "credit_score": round(credit_score, 0)})
            connection.commit()

    return round(credit_score, 0)

def calculate_loan_info(p_customer_id):
    # Define the query to calculate loan info
    query = text("SELECT total_loan_amount, total_repayment, outstanding_loan_balance FROM calculate_loan_info(:customer_id)")
    with engine.connect() as connection:
        result = connection.execute(query, {"customer_id": p_customer_id})
        row = result.fetchone()
        return row[0], row[1], row[2]

def get_credit_card_balance(p_customer_id):
    # Define the query to get credit card balance
    query = text("SELECT credit_card_balance FROM get_credit_card_balance(:customer_id)")
    with engine.connect() as connection:
        result = connection.execute(query, {"customer_id": p_customer_id})
        row = result.fetchone()
        return row[0]

def count_late_payments(p_customer_id):
    # Define the query to count late payments
    query = text("SELECT late_pay_count FROM count_late_payments(:customer_id)")
    with engine.connect() as connection:
        result = connection.execute(query, {"customer_id": p_customer_id})
        row = result.fetchone()
        return row[0]

def calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count):
    # Define the query to calculate credit score value
    query = text("SELECT calculate_credit_score_value(:total_loan_amount, :total_repayment, :credit_card_balance, :late_pay_count)")
    with engine.connect() as connection:
        result = connection.execute(query, {"total_loan_amount": total_loan_amount, "total_repayment": total_repayment, "credit_card_balance": credit_card_balance, "late_pay_count": late_pay_count})
        row = result.fetchone()
        return row[0]
