from datetime import datetime
import csv

class ExpenseTracker:
    def __init__(self, username):
        self.username = username
        self.filename = f'users/{username}.csv'

    def _calculate_expenses(self):
        total_expense = 0
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    total_expense += int(row[4])
        except FileNotFoundError:
            pass
        return total_expense

    def add_expense(self, name, expense_type, amount):
        total_expense = self._calculate_expenses()
        total_expense += int(amount)
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.username, total_expense, name, expense_type, amount, current_datetime])
