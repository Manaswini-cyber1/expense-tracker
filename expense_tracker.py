import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    expenses = load_expenses()

    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "item": item,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nExpense List:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['item']} - ₹{expense['amount']}")

def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses available.")
        return

    view_expenses()

    choice = int(input("Enter expense number to delete: ")) - 1

    if 0 <= choice < len(expenses):
        deleted = expenses.pop(choice)
        save_expenses(expenses)
        print(f"{deleted['item']} deleted successfully!")
    else:
        print("Invalid choice.")

def total_spending():
    expenses = load_expenses()
    total = sum(expense["amount"] for expense in expenses)
    print("Total Spending: ₹", total)

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        total_spending()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")