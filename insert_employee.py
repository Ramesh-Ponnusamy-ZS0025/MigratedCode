
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def insert_employee(emp_name, emp_salary):
    conn = engine.connect()
    
    try:
        query = text("INSERT INTO employees (name, salary) VALUES (:emp_name, :emp_salary)")
        conn.execute(query, {'emp_name': emp_name, 'emp_salary': emp_salary})
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

# Note: No ORM models are used, and the function returns no output as per the original procedure.
