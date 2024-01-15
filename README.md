# Expense Analyser

[ something about the app ]

## Set up
To get started, clone this repository, then run the following command.
```
pipenv install
```
This should install all the required dependencies from the pipfile.

## Running
You can start using the app by running the python main file in app folder. Followed by a command.

```
pipenv run python app/main.py < command >
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
This example will show you how to add a new income into the app.

```
pipenv run python app/main.py add_income
```

This above command should prompt you for inputs related to income as follows:
```
enter income: 4000
enter month: jan
enter year: 2025
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
