import unittest
from unittest.mock import patch

from expense_tracker.tracker import (
    add_expense,
    total_expenses,
)


class TestExpenseTracker(unittest.TestCase):

    def test_add_expense(self):
        expenses = []

        with patch("builtins.input", side_effect=["Tiffin", "100"]):
            add_expense(expenses)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["name"], "Tiffin")
        self.assertEqual(expenses[0]["amount"], 100.0)

    def test_add_expense_rejects_invalid_amount(self):
        expenses = []

        with patch("builtins.input", side_effect=["Tiffin", "abc"]):
            add_expense(expenses)

        self.assertEqual(len(expenses), 0)

    def test_total_expenses(self):
        expenses = [
            {"name": "Tiffin", "amount": 100.0},
            {"name": "Bus", "amount": 50.0},
        ]

        with patch("builtins.print") as mocked_print:
            total_expenses(expenses)

        mocked_print.assert_called_once_with("Total Expenses: ₹150.00")


if __name__ == "__main__":
    unittest.main()

