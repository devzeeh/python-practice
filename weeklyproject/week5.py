import json
from pathlib import Path

file_path = Path("weeklyproject/expenses.json")

# Load existing expenses on startup
if file_path.exists():
    with open(file_path, "r") as file:
        expenses = json.load(file)
else:
    expenses = []


def save_expenses():
    with open(file_path, "w") as file:
        json.dump(expenses, file, indent=4)


while True:
    option = int(input("\n1. Add Expense  2. View All  3. Total Spent  4. Exit\nChoose: "))

    if option == 4:
        print("Goodbye!")
        break

    elif option == 1:
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        expenses.append({"description": description, "amount": amount, "date": date})
        save_expenses()
        print("Expense added!")

    elif option == 2:
        if not expenses:
            print("No expenses yet.")
        for expense in expenses:
            print(f"{expense['date']} - {expense['description']}: ${expense['amount']:.2f}")

    elif option == 3:
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total spent: ${total:.2f}")

    else:
        print("Please choose a valid option (1-4).")