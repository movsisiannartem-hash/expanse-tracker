import argparse
import csv
from pathlib import Path
from datetime import date
import math


parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

parser_add = subparser.add_parser("add")
parser_add.add_argument("--description", type=str, required=True)
parser_add.add_argument("--amount", type=float, required=True)

parser_list = subparser.add_parser("list")

parser_summary = subparser.add_parser("summary")
parser_summary.add_argument("--month", type=int, required=False)

parser_update = subparser.add_parser("update")
parser_update.add_argument("--id", type=int, required=True)
parser_update.add_argument("--description", type=str)
parser_update.add_argument("--amount", type=float)

parser_delete = subparser.add_parser("delete")
parser_delete.add_argument("--id", type=int, required=True)

args = parser.parse_args()



path = Path("expenses.csv")

def load_expenses():

    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            expenses = list(reader)
            return expenses

    else:

        with open("expenses.csv", "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "date", "description", "amount"])
            writer.writeheader()

            return []



def save_expenses(expenses):

    with open("expenses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "date", "description", "amount"])
        writer.writeheader()
        writer.writerows(expenses)



def add(description, amount):

    description = description.strip()

    if not math.isfinite(amount):
        print("Amount must be finite")
        return

    if amount <= 0:
        print("Amount must be greater than 0")
        return


    if description == "":
        print("Description cannot be empty")
        return


    expenses = load_expenses()


    if len(expenses) == 0:
        expenses_id = 1
    else:
        expenses_id = max([int(expense["id"]) for expense in expenses]) + 1

    expanse_date = date.today().isoformat()




    expenses.append({
        "id": expenses_id,
        "date": expanse_date,
        "description": description,
        "amount": amount
    })
    save_expenses(expenses)
    print("Saving expenses is done")



def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found")
        return

    for expense in expenses:
        print(f'{expense["id"]}. {expense["date"]} - {expense["description"]}: ${float(expense["amount"]):.2f}')



def summary(month=None):
    total = 0
    expenses = load_expenses()




    if month:
        if not 0 < month <= 12:
            print("Month must be between 1 and 12")
            return
        for expense in expenses:

            if date.fromisoformat(expense["date"]).month == month and date.fromisoformat(expense["date"]).year == date.today().year:
                total += float(expense["amount"])


    else:
        for expense in expenses:
            total += float(expense["amount"])

    print(f"Total expenses: ${total:.2f}")



def delete(expense_id):
    expenses = load_expenses()

    if not expenses:
        print("No expenses found")
        return

    if not any(int(expense["id"]) == expense_id for expense in expenses):
        print("Expense not found")
        return

    for expense in expenses:
        if int(expense["id"]) == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Deleting expense is done")
            return



def update(expense_id, description=None, amount=None):
    expenses = load_expenses()




    if not expenses:
        print("No expenses found")
        return

    if description is None and amount is None:
        print("Provide a description or an amount to update")
        return

    if description is not None:
        description = description.strip()



        if description == "":
            print("Description cannot be empty")
            return

    if amount is not None and not math.isfinite(amount):
        print("Amount must be finite")
        return

    if amount is not None and amount <= 0:
        print("Amount must be greater than 0")
        return



    for expense in expenses:
        if int(expense["id"]) == expense_id:

            if description is not None:
                expense["description"] = description
            if amount is not None:
                expense["amount"] = amount

            save_expenses(expenses)
            print("Updating expense is done")
            return
    print("ID not found")


if args.command == "add":
    add(args.description, args.amount)
elif args.command == "list":
    list_expenses()
elif args.command == "summary":
    summary(args.month)
elif args.command == "delete":
    delete(args.id)
elif args.command == "update":
    update(args.id, args.description, args.amount)





