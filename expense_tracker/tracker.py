import json
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "expenses.json"


def load_expenses():
    """Load expenses from the JSON file."""

    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: Expense file contains invalid JSON.")
        return []

    except OSError as error:
        print(f"Error reading file: {error}")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

    except OSError as error:
        print(f"Error saving expenses: {error}")


def add_expense(expenses):
    """Add a new expense."""

    name = input("Enter expense name: ").strip()

    if not name:
        print("Error: Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return

    except ValueError:
        print("Error: Enter a valid number.")
        return

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added and saved successfully!")


def view_expenses(expenses):
    """Display all expenses."""

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ₹{expense['amount']:.2f}")


def total_expenses(expenses):
    """Calculate total expenses."""

    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: ₹{total:.2f}")

