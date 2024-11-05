
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def insert_employee(emp_name, emp_salary):
    connection = engine.connect()
    try:
        query = text("INSERT INTO employees (name, salary) VALUES (:emp_name, :emp_salary)")
        connection.execute(query, {"emp_name": emp_name, "emp_salary": emp_salary})
        connection.commit()
    finally:
        connection.close()
