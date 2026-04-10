import sqlite3

DB_PATH = "sales.db"

def connect():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee TEXT,
        department TEXT,
        city TEXT,
        revenue REAL,
        expense REAL,
        month TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = connect()
    cur = conn.cursor()

    data = [
        ("Arun", "IT", "Chennai", 50000, 20000, "Jan"),
        ("Meena", "Sales", "Chennai", 70000, 30000, "Jan"),
        ("John", "Sales", "Mumbai", 90000, 40000, "Feb"),
        ("Sara", "HR", "Delhi", 40000, 15000, "Feb"),
        ("Kiran", "IT", "Mumbai", 60000, 25000, "Mar"),
    ]

    cur.executemany("""
    INSERT INTO sales (employee, department, city, revenue, expense, month)
    VALUES (?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()