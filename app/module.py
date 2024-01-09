import sqlite3
from ui import User_input_income, User_input_expense, show_all_expenses
from typing import List, Tuple

conn = sqlite3.connect("expense.db")

cur = conn.cursor()

Expense_sum_type = List[Tuple[float]]

# get all expenses
def get_all_expenses():
    sql = "SELECT * FROM expenses"
    result = cur.execute(sql)
    return result.fetchall()


# add an income record to db
def add_income(income: User_input_income) -> None:
    sql = f"INSERT INTO incomes( income, month, year ) VALUES ( '{income.income}', '{income.month}', '{income.year}' )"

    cur.execute(sql)
    conn.commit()


# add an expense record to db
def add_expense(expense: User_input_expense) -> None:
    sql = f"INSERT INTO expenses(title, category, amount, month, year) VALUES ( '{expense.title}', '{expense.category}', {expense.amount}, '{expense.month}', '{expense.year}')"

    cur.execute(sql)
    conn.commit()

# get sum of all expenses of a month
def get_expense_sum(month: str, year: str) -> float:
    sql = f"SELECT SUM(amount) FROM expenses WHERE month = '{month}' and year = '{year}'"
    result = cur.execute(sql)

    return result.fetchone()[0]

# get income of a month
def get_income(month: str, year: str) -> float:
    sql = f"SELECT income FROM incomes WHERE month = '{month}' and year = '{year}'"
    result = cur.execute(sql)
    return result.fetchone()[0]


# get sum of all expense of same category for a month
def get_expense_sum_by_category(category: str, month: str, year: str) -> float:
    sql = f'''SELECT SUM(amount) 
                FROM expenses 
                GROUP BY year, month, category 
                HAVING year = '{year}' AND month = '{month}' AND category = '{category}' '''

    result = cur.execute(sql)
    try:
        sum, = result.fetchone()
        # print(sum)
        return sum
    except Exception as e: 
        # print(f"error occured {e}")
        return 0.0


def get_month_expense_summary(month: str, year: str):
    sql = f'''select category, sum(amount)
            from expenses
            group by year, month, category
            having year = "2024" and month = "jan"
            order by sum(amount) desc '''
    
    result = cur.execute(sql)
    result = result.fetchall()[0]
    print(result)

# get_month_expense_summary("jan", "2024")
    




