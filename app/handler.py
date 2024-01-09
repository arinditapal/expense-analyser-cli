from typing import Tuple
from datetime import datetime
import calendar
from math import fabs
from module import (
    add_income,
    add_expense,
    get_expense_sum,
    get_income,
    get_expense_sum_by_category,
)
from ui import (
    Expense, 
    take_income, 
    take_expense, 
    print_budget, 
    Category, 
    print_trend
)


# tuple(id, title, category, amount) to Expense()
def tuple_to_expense(expense_tuple):
    expenses = []
    for tuple_expense in expense_tuple:
        id, title, category, amount, month, year = tuple_expense
        expense = Expense(id, title, category, amount, month, year)
        expenses.append(expense)
    return expenses


# add income command handler
def add_income_handler() -> None:
    income = take_income()
    add_income(income)


# add expense command handler
def add_expense_handler() -> None:
    expense = take_expense()
    add_expense(expense)


# analyse budget
def budget_analyser(budget: float) -> str:
    if budget > 0:
        return "LESS"
    if budget < 0:
        return "MORE"
    return "SAME"


# budget show handler
def show_budget_handler() -> None:
    print("Give following info, press enter for current month budget: ")
    month = input("\nWhich month's budget you want to see?  [jan, feb...]: ")
    year = input("Which year  like: [2024, 2023...]: ")

    if not month:
        month = (datetime.now().strftime("%b")).lower()
        year = str(datetime.now().year)

    expenses_sum = get_expense_sum(month, year)
    income = get_income(month, year)

    budget = round(income - expenses_sum, 3)

    print_budget(
        income, expenses_sum, fabs(budget), 
        budget_analyser(budget), month, year
    )


# find previous month name, number, year
def find_previous_month(current_year: int) -> Tuple[str, int]:
    current_month_number = datetime.now().month

    previous_month_number = 0
    previous_year = 0

    # finding previous month name
    if current_month_number - 1 != 0:
        previous_month_number = current_month_number - 1
        previous_year = current_year
    else:
        previous_month_number = 12
        previous_year = current_year - 1

    previous_month_name = (calendar.month_abbr[previous_month_number]).lower()

    return (previous_month_name, previous_year)


# show trend handler
def show_trends_handler() -> None:
    current_month_name = (datetime.now().strftime("%b")).lower()
    current_year = str(datetime.now().year)

    previous_month_name, previous_year = find_previous_month(int(current_year))

    for i in range(4):
        category = Category(i).name

        # getting expense of current month
        current_month_expense_sum = get_expense_sum_by_category(
            category, current_month_name, current_year
        )

        # getting expense of previous month
        previous_month_expense_sum = get_expense_sum_by_category(
            category, previous_month_name, str(previous_year)
        )

        print_trend(
            category, current_month_expense_sum, previous_month_expense_sum
            )
