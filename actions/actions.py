from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = "sales.db"

def get_conn():
    return sqlite3.connect(DB_PATH)


class action_total_revenue(Action):
    def name(self):
        return "action_total_revenue"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT SUM(revenue) as total FROM sales", conn)
        total = df["total"][0]
        dispatcher.utter_message(f"Total Revenue: ₹{total}")
        return []


class action_profit(Action):
    def name(self):
        return "action_profit"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT SUM(revenue - expense) as profit FROM sales", conn)
        dispatcher.utter_message(f"Total Profit: ₹{df['profit'][0]}")
        return []


class action_expense(Action):
    def name(self):
        return "action_expense"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT SUM(expense) as expense FROM sales", conn)
        dispatcher.utter_message(f"Total Expense: ₹{df['expense'][0]}")
        return []


class action_employee_count(Action):
    def name(self):
        return "action_employee_count"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT department, COUNT(*) as count FROM sales GROUP BY department", conn)

        msg = "\n".join([f"{row['department']}: {row['count']}" for _, row in df.iterrows()])
        dispatcher.utter_message(msg)
        return []


class action_bar_chart(Action):
    def name(self):
        return "action_bar_chart"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT city, SUM(revenue) as revenue FROM sales GROUP BY city", conn)

        os.makedirs("charts", exist_ok=True)

        plt.bar(df["city"], df["revenue"])
        path = "charts/bar_chart.png"
        plt.savefig(path)
        plt.close()

        dispatcher.utter_message(f"Bar chart saved at {path}")
        return []


class action_pie_chart(Action):
    def name(self):
        return "action_pie_chart"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT city, SUM(revenue) as revenue FROM sales GROUP BY city", conn)

        os.makedirs("charts", exist_ok=True)

        plt.pie(df["revenue"], labels=df["city"], autopct="%1.1f%%")
        path = "charts/pie_chart.png"
        plt.savefig(path)
        plt.close()

        dispatcher.utter_message(f"Pie chart saved at {path}")
        return []


class action_export_excel(Action):
    def name(self):
        return "action_export_excel"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT * FROM sales", conn)

        os.makedirs("reports", exist_ok=True)
        path = "reports/sales_report.xlsx"
        df.to_excel(path, index=False)

        dispatcher.utter_message(f"Excel report saved at {path}")
        return []


class action_export_csv(Action):
    def name(self):
        return "action_export_csv"

    def run(self, dispatcher, tracker, domain):
        conn = get_conn()
        df = pd.read_sql_query("SELECT * FROM sales", conn)

        os.makedirs("reports", exist_ok=True)
        path = "reports/sales_report.csv"
        df.to_csv(path, index=False)

        dispatcher.utter_message(f"CSV report saved at {path}")
        return []