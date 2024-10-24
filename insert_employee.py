
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def insert_employee(emp_name, emp_salary):
    conn = engine.connect()
    try:
        insert_query = text("""
            INSERT INTO employees (name, salary) VALUES (:emp_name, :emp_salary)
        """)
        conn.execute(insert_query, {"emp_name": emp_name, "emp_salary": emp_salary})
        conn.commit()
    except psycopg2.Error as e:
        raise e
    finally:
        conn.close()
    return None
