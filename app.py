from flask import Flask, render_template, request, redirect, url_for
from login import UserAuthentication
from registration import UserRegistration
from expense_tracker import ExpenseTracker
import csv

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user and fetch latest expense data
        latest_expense = UserAuthentication.authenticate_user(username, password)

        if latest_expense:
            total_expense = latest_expense

            # Redirect to user dashboard page if authentication succeeds
            return redirect(url_for('dashboard', username=username, total_expense=total_expense))
        else:
            # Redirect to login failed page if authentication fails
            return redirect(url_for('login_failed', error='Invalid username or password. Please try again.'))

    # Render the login page template for GET requests
    return render_template('login.html')

@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    # Retrieve total expenses from URL parameters
    total_expense = request.args.get('total_expense')

    # If values are not passed as URL parameters, set them to None
    if total_expense is None:
        total_expense = 0
    
    current_month = 'April'  # Example: Replace with actual current month

    if request.method == 'POST':
        expense_name = request.form['name']
        expense_type = request.form['expense_type']
        expense_amount = int(request.form['amount'])
        # Create an ExpenseTracker object for the user
        tracker = ExpenseTracker(username)
        tracker.add_expense(expense_name, expense_type, expense_amount)
        # Recalculate total expenses after adding the new expense
        total_expense = tracker._calculate_expenses()
    
    return render_template('dashboard.html', username=username, total_expense=total_expense, current_month=current_month)

@app.route('/register', methods=['GET', 'POST'])  # Add route for registration
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Register user
        if UserRegistration.register_user(username, password):
            # Redirect to login page after successful registration
            return redirect(url_for('login'))
        else:
            # Redirect to registration failed page if registration fails
            return redirect(url_for('registration_failed', error='Username already exists. Please choose another username.'))

    # Render the registration page template for GET requests
    return render_template('register.html')

@app.route('/user/<username>')
def user_account(username):
    # Here you can fetch user-specific data (e.g., total expense, total monthly expense) from the database
    # For now, let's just render a dummy template
    return render_template('user_account.html', username=username)

@app.route('/login-failed')
def login_failed():
    error = request.args.get('error', 'Login failed.')
    return render_template('login_failed.html', error=error)

@app.route('/registration-failed')
def registration_failed():
    error = request.args.get('error', 'Username already exists. Please choose another username.')
    return render_template('registration_failed.html', error=error)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        username = request.form['username']  # Make sure this key matches the name attribute in the HTML form
        name = request.form['name']          # Make sure this key matches the name attribute in the HTML form
        expense_type = request.form['expense_type']  # Make sure this key matches the name attribute in the HTML form
        amount = int(request.form['amount']) # Make sure this key matches the name attribute in the HTML form

        # Create an ExpenseTracker object for the user
        tracker = ExpenseTracker(username)
        tracker.add_expense(name, expense_type, amount)

        # Redirect to the dashboard page after adding the expense
        return redirect(url_for('dashboard', username=username))

    # If the request method is not POST, redirect to the homepage
    return redirect(url_for('index'))

@app.route('/expense_history/<username>')
def expense_history(username):
    # Load expense history data from the user's CSV file
    try:
        with open(f'users/{username}.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            expense_history = list(reader)
    except FileNotFoundError:
        expense_history = []

    return render_template('expense_history.html', username=username, expense_history=expense_history)


if __name__ == '__main__':
    app.run(debug=True)
