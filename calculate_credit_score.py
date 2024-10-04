
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def calculate_customer_credit_score(p_customer_id):
    conn = engine.connect()
    try:
        # Call the procedures to get necessary data
        total_loan_amount = None
        total_repayment = None
        outstanding_loan_balance = None
        credit_card_balance = None
        late_pay_count = None

        query = text("SELECT * FROM calculate_loan_info(:p_customer_id, :total_loan_amount, :total_repayment, :outstanding_loan_balance)")
        result = conn.execute(query, {'p_customer_id': p_customer_id, 'total_loan_amount': total_loan_amount, 'total_repayment': total_repayment, 'outstanding_loan_balance': outstanding_loan_balance})
        for row in result:
            total_loan_amount = row[0]
            total_repayment = row[1]
            outstanding_loan_balance = row[2]

        query = text("SELECT * FROM get_credit_card_balance(:p_customer_id, :credit_card_balance)")
        result = conn.execute(query, {'p_customer_id': p_customer_id, 'credit_card_balance': credit_card_balance})
        for row in result:
            credit_card_balance = row[0]

        query = text("SELECT * FROM count_late_payments(:p_customer_id, :late_pay_count)")
        result = conn.execute(query, {'p_customer_id': p_customer_id, 'late_pay_count': late_pay_count})
        for row in result:
            late_pay_count = row[0]

        v_credit_score = None
        query = text("SELECT * FROM calculate_credit_score_value(:total_loan_amount, :total_repayment, :credit_card_balance, :late_pay_count, :v_credit_score)")
        result = conn.execute(query, {'total_loan_amount': total_loan_amount, 'total_repayment': total_repayment, 'credit_card_balance': credit_card_balance, 'late_pay_count': late_pay_count, 'v_credit_score': v_credit_score})
        for row in result:
            v_credit_score = row[0]

        # Update the customer's credit score
        query = text("UPDATE customers SET credit_score = ROUND(:v_credit_score, 0) WHERE id = :p_customer_id")
        conn.execute(query, {'v_credit_score': v_credit_score, 'p_customer_id': p_customer_id})
        conn.commit()

        # Optionally log very low scores
        if v_credit_score < 500:
            query = text("INSERT INTO credit_score_alerts (customer_id, credit_score, created_at) VALUES (:p_customer_id, ROUND(:v_credit_score, 0), NOW())")
            conn.execute(query, {'p_customer_id': p_customer_id, 'v_credit_score': v_credit_score})
            conn.commit()

        return v_credit_score
    finally:
        conn.close()
