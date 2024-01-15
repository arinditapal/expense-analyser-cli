# Expense Analyser

This is an Expense Analyser app, which will keep track of you expenses and income for a month, then give you analysis of the budget left. It can also show you trend in your expenditure for current month against previous months.

## Set up
To get started, clone this repository, then run the following command.
```
pipenv install
```
This should install all the required dependencies from the pipfile.

## Running
You can start using the app by running the python main file in app folder. Followed by a command.

```
pipenv run python app/main.py <command>
```

You can see the list of commands use with the app in the --help option.

```
pipenv run python app/main.py --help
```

This above command will list all the commands.

## Commands
Little description about all the commands and what they do.

* add_income
    - Add a new income of a month.
* add_expense
    - Add a new expense.
* show_budget
    - Show the budget of a month after subtracting expense from income that that month.
* show_trends
    - shows the trend in your expenditure in all category from current and previous month.


## Example
0. To add expense
```shell
$  pipenv run python app/main.py add_expense
Enter title: cream bread
Different category of expense are:
        0 - food
        1 - gadget
        2 - transport
        3 - fun
Enter category number[0 - 3]: 0
Enter amount: 30
Enter month: jan
Enter year, ex: '2024': 2024
```

1. To add income
```shell
$  pipenv run python app/main.py add_income
enter income: 5000
enter month: feb
enter year: 2024
```

2. To see budget
```shell
$  pipenv run python app/main.py show_budget
Give following info, press enter for current month budget:

Which month's budget you want to see?  [jan, feb...]:
Which year  like: [2024, 2023...]:

        Your budget analysis is a follows

You spent LESS in jan of 2024 by ₹545.0.

                       Budget of current month
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃        Income        ┃       Expense        ┃        Budget        ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│        ₹800.0        │        ₹255.0        │        ₹545.0        │
└──────────────────────┴──────────────────────┴──────────────────────┘
```

3. To see trend
```shell
$  pipenv run python app/main.py show_trends

 Trends in your spending habits in FOOD for current and past months are:

                 Trend in food
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃    Previous Month    ┃    Current Month     ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│         ₹0.0         │        ₹225.0        │
└──────────────────────┴──────────────────────┘

 Trends in your spending habits in GADGET for current and past months are:

                Trend in gadget
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃    Previous Month    ┃    Current Month     ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│         ₹0.0         │         ₹0.0         │
└──────────────────────┴──────────────────────┘

 Trends in your spending habits in TRANSPORT for current and past months are:

              Trend in transport
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃    Previous Month    ┃    Current Month     ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│         ₹0.0         │        ₹20.0         │
└──────────────────────┴──────────────────────┘

 Trends in your spending habits in FUN for current and past months are:

                 Trend in fun
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃    Previous Month    ┃    Current Month     ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│         ₹0.0         │        ₹10.0         │
└──────────────────────┴──────────────────────┘
```

> ## Assumptions
> The months that you enter has to be in all small letters and abbrated to 3 letters only, like below
> 
>
> - jan
> - feb
> - mar
> - apr
> - may
> - jun
> - jul 
> - aug
> - sep
> - oct
> - nov
> - dec
