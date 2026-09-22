expenses = []
def add_expense(amount,category,note):
    expense = {
        "Price": amount,
        "Category": category,
        "Note": note
    }
    expenses.append(expense)

print(expenses)
