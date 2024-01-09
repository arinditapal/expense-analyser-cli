from argparse import ArgumentParser
from handler import add_expense_handler, add_income_handler, show_budget_handler, show_trends_handler

parser = ArgumentParser()

parser.add_argument("operation", 
                    help="operation you wanna perform", 
                    choices=[
                        "add_income", 
                        "add_expense", 
                        "show_budget", 
                        "show_trends"
                    ])

args = parser.parse_args()


if args.operation == "add_expense":
    add_expense_handler()
elif args.operation == "add_income":
    add_income_handler()
elif args.operation == "show_budget":
    show_budget_handler()
elif args.operation == "show_trends":
    show_trends_handler()


# Todos
# if nothing is given in analysis then show the analysis of current month.
# put some explaination in trend showing
# show the expenses
