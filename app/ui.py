from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
from typing import List
from enum import Enum
from rich import print


# expense schema
@dataclass
class Expense:
    id: int
    title: str
    category: str
    amount: float
    month: str
    year: str


# income schema
@dataclass
class Income:
    id: int
    income: float
    month: str
    year: str


# input expense schema
@dataclass
class User_input_expense:
    title: str
    category: str
    amount: float
    month: str
    year: str


# input income schema
@dataclass
class User_input_income:
    income: float
    month: str
    year: str


# category and its id
class Category(Enum):
    food = 0
    gadget = 1
    transport = 2
    fun = 3


# takes income value from user
def take_income() -> User_input_income:
    income = float(input("enter income: "))
    month = input("enter month: ")
    year = input("enter year: ")

    return User_input_income(income, month, year)


# takes an new expense from user
def take_expense() -> User_input_expense:
    title = input("Enter title: ")

    print("Different category of expense are:")
    for i in range(4):
        print(f"\t{i} - {Category(i).name}")

    category_id = int(input("Enter category number[0 - 3]: "))
    category = Category(category_id).name

    amount = float(input("Enter amount: "))
    month = input("Enter month: ")
    year = input("Enter year, ex: '2024': ")

    return User_input_expense(title, category, amount, month, year)


# show list of expenses to user
def show_all_expenses(expenses: List[Expense]) -> None:

    expense_table = Table(title="Expenses", border_style="yellow")

    # fields of the display expense table ( table columns )
    expense_table.add_column("id", style="green")
    expense_table.add_column("title")
    expense_table.add_column("category")
    expense_table.add_column("amount", style="red")

    # adding expenses to the display expense table ( table rows )
    for expense in expenses:
        amount = "₹ " + str(expense.amount)
        expense_table.add_row(str(expense.id), expense.title, expense.category, amount)
    console = Console()
    console.print(expense_table)


# prints budget for user
def print_budget(income: float, expense: float, budget: float, message: str, month: str, year: str):
    console = Console()
    console.print("\n\tYour budget analysis is a follows\n", style="blue")

    print(f"You spent [yellow blue]{message}[/] in [bold blue]{month}[/] of [blue]{year}[/] by ₹{budget}.\n")

    budget_table = Table(title="Budget of current month", border_style="green")

    # fields
    budget_table.add_column("Income", min_width=20, justify="center", vertical="middle", header_style="yellow")
    budget_table.add_column("Expense", min_width=20, justify="center", vertical="middle", header_style="yellow")
    budget_table.add_column("Budget", min_width=20, justify="center", vertical="middle", header_style="yellow")

    # row
    budget_table.add_row( f"₹{income}", f"₹{expense}", f"₹{budget}")

    console = Console()
    console.print(budget_table)


# this will summarise the expense of a month
def expense_summary(category: str, category_amount: float, month: str, year: str):

    console = Console()
    month_year = month + " " + year
    console.print(f'You spent THE MOST in "{category}" in {month_year}', style="green")
    console.print(f"\tby amount: [yellow]₹{category_amount}[/]", style="green")


# printing trends s
def print_trend(category, current_month_expense, previous_month_expense):
    console = Console()
    console.print(f"\n Trends in your spending habits in {category.upper()} for current and past months are: \n", style="blue")

    # # table for display of the trend
    category_table = Table(title=f"Trend in {category}", style="green")

    # column of table
    category_table.add_column("Previous Month",min_width=20, justify="center", vertical="middle", header_style="yellow")
    category_table.add_column("Current Month", min_width=20, justify="center", vertical="middle", header_style="yellow")

    # row of table 
    category_table.add_row(f"₹{previous_month_expense}", f"₹{current_month_expense}")

    console = Console()
    console.print(category_table)