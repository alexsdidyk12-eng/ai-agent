from db import add_expense, get_all_expenses, delete_expense_by_id,delete_last_expense,update_expense
from parser import parse_expense

def add_expense_tool(user_input):
    amount, category=parse_expense(user_input)
    
    if not amount or not category:
        return("Ya ne poluchil infu o cene i categorii")
    else:
        return add_expense(amount, category)
    
def get_all_expenses_tool():
    return get_all_expenses()
def delete_expense_tool(user_input):
    text = user_input.lower()
    
    if "posled" in user_input or "last" in user_input:
        return delete_last_expense()
    words=text.split()
    
    for word in words:
        if word.isdigit():
            return delete_expense_by_id(int(word))
    
    return"napishu id dlya udalenia"

def update_expense_tool(user_input):
    words=user_input.lower().split()
    
    numbers=[]
    
    for word in words:
        if word.isdigit():
            numbers.append(int(word))
            
    if len(numbers)<2:
            return"You ,ust input 2 numbers! Id and new amount!"
    expense_id=numbers[0]
    new_amount=numbers[1]
        
    return update_expense(expense_id, new_amount)
    
    
    


