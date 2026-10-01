
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


while True:

    question = input("What do you want to do? (add/remove/list/quit): ")
    if question.lower() == "add":
        expenses = load_expenses()
        while True:
            try:
                amount = float(input("Enter the amount: "))
                break
            except ValueError:
                print("Invalid format. Try again")

        category = input("Enter the category: ")
        note = input("Enter a note: ")
        

        add_expense(amount, category, note)

        save_expenses(expenses)

        print("The expenses are:",  expenses)
        
        break

    elif question.lower() == "remove":

        expenses = load_expenses()
        while True:
            try:
                index = int(input("Which element do you want to remove? (answer only in digits)"))
                break
            except ValueError:
                print("Invalid format.")
        
        removed_expenses = expenses.pop(index)
        print(expenses)
        
        break 

    elif question.lower() == 'list':

        expenses = load_expenses()
        for i, e in enumerate(expenses):
            print(i,e)

    elif question.lower() == 'quit':
        print("Process terminated.")
        break
    
    else:
        retry = input("Invalid option. Do you want to try again? (y/n)")
        if retry.lower() == 'y':
            pass
        else:
            print("Process terminated..")
            
            break
    
