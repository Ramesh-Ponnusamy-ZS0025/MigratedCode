
from config import engine
from sqlalchemy import text
import pandas as pd
import psycopg2

def insert_employee(emp_name, emp_salary):
    connection = engine.connect()
    try:
        query = text("INSERT INTO employees (name, salary) VALUES (:emp_name, :emp_salary)")
        result = connection.execute(query, {"emp_name": emp_name, "emp_salary": emp_salary})
        connection.commit()
        return result.rowcount
    except psycopg2.Error as e:
        raise e
    finally:
        connection.close()
