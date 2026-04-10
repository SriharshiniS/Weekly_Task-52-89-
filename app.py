from database.db import create_table, insert_sample_data
import sqlite3
import pandas as pd

DB_PATH = "sales.db"


# -----------------------------
# INIT DATABASE
# -----------------------------
def init_db():
    create_table()
    insert_sample_data()
    print("Database created and sample data inserted.")


# -----------------------------
# CONNECT DB
# -----------------------------
def get_conn():
    return sqlite3.connect(DB_PATH)


# -----------------------------
# SAMPLE QUERIES (for testing without Rasa)
# -----------------------------
def total_revenue():
    conn = get_conn()
    df = pd.read_sql_query("SELECT SUM(revenue) AS total FROM sales", conn)
    print("Total Revenue:", df["total"][0])


def total_profit():
    conn = get_conn()
    df = pd.read_sql_query("SELECT SUM(revenue - expense) AS profit FROM sales", conn)
    print("Total Profit:", df["profit"][0])


def expense_total():
    conn = get_conn()
    df = pd.read_sql_query("SELECT SUM(expense) AS expense FROM sales", conn)
    print("Total Expense:", df["expense"][0])


def employee_by_department():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT department, COUNT(*) as count
        FROM sales
        GROUP BY department
    """, conn)

    print(df)


def top_city():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT city, SUM(revenue) as revenue
        FROM sales
        GROUP BY city
        ORDER BY revenue DESC
        LIMIT 1
    """, conn)

    print("Top City:", df.iloc[0])


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print("🚀 Starting Sales Chatbot Backend Test")

    init_db()

    print("\n--- Testing Queries ---")
    total_revenue()
    total_profit()
    expense_total()
    employee_by_department()
    top_city()