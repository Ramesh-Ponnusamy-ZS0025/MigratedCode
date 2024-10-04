Python
from config import engine
import sqlalchemy as db
import pandas as pd
import psycopg2

def update_customer_credit_score(customer_id):
    with engine.connect() as connection:
        # Calculate loan info
        query = text("""
            SELECT * FROM calculate_loan_info(:customer_id, :total_loan_amount, :total_repayment, :outstanding_loan_balance)
        """)
        result = connection.execute(query, {'customer_id': customer_id, 'total_loan_amount': 0, 'total_repayment': 0, 'outstanding_loan_balance': 0})
        total_loan_amount, total_repayment, outstanding_loan_balance = result.fetchone()

        # Get credit card balance
        query = text("""
            SELECT * FROM get_credit_card_balance(:customer_id)
        """)
        result = connection.execute(query, {'customer_id': customer_id})
        credit_card_balance, = result.fetchone()

        # Count late payments
        query = text("""
            SELECT * FROM count_late_payments(:customer_id)
        """)
        result = connection.execute(query, {'customer_id': customer_id})
        late_pay_count, = result.fetchone()

        # Calculate credit score
        query = text("""
            SELECT * FROM calculate_credit_score_value(:total_loan_amount, :total_repayment, :credit_card_balance, :late_pay_count)
        """)
        result = connection.execute(query, {'total_loan_amount': total_loan_amount, 'total_repayment': total_repayment, 'credit_card_balance': credit_card_balance, 'late_pay_count': late_pay_count})
        credit_score, = result.fetchone()

        # Update customer's credit score
        query = text("""
            UPDATE customers
            SET credit_score = ROUND(:credit_score, 0)
            WHERE id = :customer_id
        """)
        connection.execute(query, {'credit_score': credit_score, 'customer_id': customer_id})
        connection.commit()

        # Optionally log very low scores
        if credit_score < 500:
            query = text("""
                INSERT INTO credit_score_alerts (customer_id, credit_score, created_at)
                VALUES (:customer_id, ROUND(:credit_score, 0), NOW())
            """)
            connection.execute(query, {'customer_id': customer_id, 'credit_score': credit_score})
            connection.commit()

    return credit_score
