# Daily Expense Tracker

The Daily Expense Tracker is a simple web application designed to help users track their daily expenses conveniently. It provides a user-friendly interface for managing expenses, registration, and login functionality.

## Features

- User registration and login system.
- Personalized expense tracking for each registered user.
- User-friendly web interface for adding and viewing expenses.
- Data stored in CSV format for easy retrieval and manipulation.

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python
- **Framework:** Flask

## Project Structure

- `app.py`: The main Flask application file containing the backend logic.
- `templates/`: Directory containing HTML templates for the frontend.
- `static/`: Directory containing static assets such as CSS stylesheets and JavaScript files.
- `users.csv`: CSV file to store user credentials.
- `users/`: Directory to store CSV files for each user's expense data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SohelPratap/p1.git
    ```

2. Install the required Python dependencies:

    ```bash
    cd p1
    python -m venv venv
    venv\Scripts\activate   # for Windows
    source venv/bin/activate   # for macOS/Linux
    pip install --upgrade pip
    pip install Flask
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage

1. Visit the main page at `/index` to register or login.
2. Use the `/register` route to create a new account.
3. Login using the credentials provided during registration.
4. Once logged in, access `/dashboard/username` to add expenses for a particular user.
5. To view expense history, navigate to `/expense-history/username`.

## Contributors

- Sohel Pratap Singh - Lead Developer
- Shrawan Kumar Bhagat
- Abhinav Nirapure
- Yuvraj Bhatkariya
- Omkar Markam

