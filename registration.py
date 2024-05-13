# registration.py

import os
import csv

class UserRegistration:
    USERS_FOLDER = 'users'
    USERS_CSV_FILE = 'users.csv'

    def __init__(self):
        pass

    @classmethod
    def initialize_user_csv(cls, username):
        # Create the users folder if it doesn't exist
        if not os.path.exists(cls.USERS_FOLDER):
            os.makedirs(cls.USERS_FOLDER)
        
        # Create a CSV file for the user
        csv_file_path = os.path.join(cls.USERS_FOLDER, f'{username}.csv')
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(['Username', 'Total Expense','Name of Expense','Type of Expense','Amount','Date Time'])
            writer.writerow([username, 0,0,0,0,0])

    @classmethod
    def check_existing_username(cls, username):
        try:
            with open(cls.USERS_CSV_FILE, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row and row[0] == username:
                        return True
        except FileNotFoundError:
            # Handle the case where the CSV file doesn't exist yet
            pass
        return False

    @classmethod
    def register_user(cls, username, password):
        if cls.check_existing_username(username):
            return False  # Username already exists
        else:
            # Initialize user CSV
            cls.initialize_user_csv(username)
            
            # Write user registration data to users.csv
            with open(cls.USERS_CSV_FILE, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([username, password])
            
            return True  # Registration successful
