# Expense Tracker

A simple Python expense tracker that stores daily expenses in a CSV file.

## Features

- Records expenses with current date
- Stores data in CSV format
- Calculates total daily expenses
- Uses Python CSV module
- Uses datetime module

## Technologies Used

- Python
- CSV
- Datetime

## Project Structure

```text
expense_tracker.py
test.csv
README.md
```

## How It Works

1. User enters expenses
2. Expenses are saved into `test.csv`
3. Program calculates total expenses
4. Data is stored with current date

## Example Output

```text
What is the expense? (type 0 to stop): 100
What is the expense? (type 0 to stop): 250
What is the expense? (type 0 to stop): 0

Your expenses today are [100, 250]
Your Total expense is 350
```

## How to Run

```bash
python expense_tracker.py
```

## Future Improvements

- Expense categories
- Monthly reports
- Data visualization using matplotlib
- SQLite database integration
- Budget tracking

## Author

Sridhar