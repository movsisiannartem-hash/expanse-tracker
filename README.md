# Expense Tracker CLI

A lightweight command-line expense tracker built with Python. Manage your personal expenses directly from the terminal with simple commands and CSV-based storage.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Interface-CLI-222222" alt="CLI">
  <img src="https://img.shields.io/badge/Storage-CSV-green" alt="CSV Storage">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Project Status">
</p>

---

## Overview

Expense Tracker CLI helps you keep track of your spending without needing a database or a graphical interface. Add expenses, review your records, update existing entries, delete them, and calculate your total spending — all from your terminal.

## Features

- **Add expenses** — record a description and amount.
- **View expenses** — display all saved records.
- **Monthly summaries** — calculate spending for a selected month.
- **Update records** — edit an expense description or amount.
- **Delete expenses** — remove records by their ID.
- **CSV storage** — keep your data in a simple, readable file.
- **Input validation** — handle invalid descriptions and amounts.

## Built With

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| `argparse` | Command-line argument parsing |
| `csv` | Reading and writing expense data |
| `pathlib` | File and path handling |
| `datetime` | Recording expense dates |
| `math` | Validating numeric amounts |

## Getting Started

### Requirements

- Python 3.10 or newer recommended
- A terminal or command-line interface

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone (https://github.com/movsisiannartem-hash/expanse-tracker.git)
cd expense-tracker
```



## Commands

### Add an expense

```bash
python main.py add --description "Lunch" --amount 15.50
```

### List all expenses

```bash
python main.py list
```

### View total spending

```bash
python main.py summary
```

### View spending for a specific month

```bash
python main.py summary --month 10
```

### Update an expense

Change its description:

```bash
python main.py update --id 1 --description "Dinner"
```

Change its amount:

```bash
python main.py update --id 1 --amount 20.00
```

### Delete an expense

```bash
python main.py delete --id 1
```

## Data Storage

All expense records are stored locally in `expenses.csv`.

Each record contains:

| Field | Description |
|---|---|
| `id` | Unique expense identifier |
| `date` | Date the expense was recorded |
| `description` | Expense description |
| `amount` | Expense amount |

The CSV file is created automatically when the application initializes its data storage.

## Example

```text
$ python main.py add --description "Coffee" --amount 4.50
Expense added successfully!

$ python main.py list
ID: 1 | Date: 2026-10-25 | Description: Coffee | Amount: 4.50

$ python main.py summary
Total expenses: 4.50
```

*Example output is illustrative; exact output depends on your implementation and saved data.*

## What I Learned

Building this project helped me practice:

- Designing a command-line interface with subcommands and arguments
- Organizing application logic into reusable functions
- Reading and writing structured data with CSV
- Validating user input and handling edge cases
- Working with dates, file paths, and numeric values
- Managing a project with Git and GitHub

## Future Improvements

- Expense categories
- Filtering expenses by date range
- Exporting reports
- Budget limits and spending alerts
- Automated tests

---
https://roadmap.sh/projects/expense-tracker
<p align="center">
  <strong>Built with Python as a personal learning project.</strong>
</p>
