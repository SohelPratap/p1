# login.py

import os
import csv

class UserAuthentication:
    USERS_CSV_FILE = 'users.csv'

    @classmethod
    def authenticate_user(cls, username, password):
        try:
            with open(cls.USERS_CSV_FILE, 'r', newline='') as users_file:
                reader = csv.reader(users_file)
                next(reader)  # Skip the header row
                for row in reader:
                    if row and len(row) >= 2 and row[0] == username and row[1] == password:
                        # If username and password match, retrieve expense data from user's CSV file
                        expense_data = cls.get_user_expense_data(username)
                        if expense_data:
                            return expense_data
                        else:
                            return None  # Failed to retrieve expense data
        except FileNotFoundError:
            # Handle the case where the CSV file doesn't exist yet
            pass
        return None  # Authentication failed

    @classmethod
    def get_user_expense_data(cls, username):
        try:
            csv_file_path = os.path.join('users', f'{username}.csv')
            with open(csv_file_path, 'r', newline='') as user_file:
                reader = csv.reader(user_file)
                next(reader)  # Skip the header row
                rows = list(reader)
                if rows:
                    # Get the latest row containing expense data
                    latest_row = rows[-1]
                    if len(latest_row) >= 2:  # Adjusted to only consider total expense
                        total_expense = latest_row[1]
                        return total_expense  # Return only total expense
        except FileNotFoundError:
            # Handle the case where the user's CSV file doesn't exist yet
            pass
        return None  # Failed to retrieve expense data
