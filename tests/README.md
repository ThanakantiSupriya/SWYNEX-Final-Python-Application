# Python Expense Tracker

A simple command-line application built using Python to manage daily expenses.

## Features

* Add new expenses
* View all saved expenses
* Calculate total expenses
* Save expense data in a JSON file
* Validate user input
* Handle file errors
* Run automated unit tests

## Technologies Used

* Python
* JSON
* Unit Testing

## Project Structure

```text
python-expense-tracker/
├── expense_tracker/
│   ├── __init__.py
│   └── tracker.py
├── tests/
│   └── test_tracker.py
├── main.py
├── expenses.json
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.10 or later
* No external packages required

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run the application:

```bash
python main.py
```

## How to Use

Choose an option from the menu:

1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit

Enter the requested details to manage your expenses.

## Run Tests

Run the following command from the project folder:

```bash
python -m unittest discover -s tests -v
```

## Data Storage

Expenses are stored in `expenses.json` and loaded when the application starts.

## Future Improvements

* Delete expenses
* Categorize expenses
* Generate monthly expense reports
* Export expenses to CSV


