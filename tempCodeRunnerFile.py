import json 

def load_expenses():
    with open("expenses.json", "r") as f:
        return json.load(f)
def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount,category,note):
    expense = {
        "Price": amount,
        "Category": category,
        "Note": note
    }
    expenses.append(expense)

def remove_expense(index):
    index = int(input("Which element do you want to remove?"))
    expense.pop(index)


while True:

    question = input("What do you want to do? (add/remove): ")
    if question.lower() == "add":
        expenses = load_expenses()

        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        note = input("Enter a note: ")
        

        add_expense(amount, category, note)

        save_expenses(expenses)

        print("The expenses are:",  expenses)

    elif question.lower() == "remove":

        expenses = remove_expense(index)
        index = int(input("Which element do you want to remove?"))



        break
