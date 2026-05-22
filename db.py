import sqlite3

def init_db():
    conn=sqlite3.connect("finance.db")
    cursor=conn.cursor()
    
    cursor.execute("""
                  create table if not exists expenses(
                      id integer primary key autoincrement,
                      amount integer,
                      category text,
                      created_at timestamp default current_timestamp
                  ) 
                   """)
    
    #save
    conn.commit()
    conn.close()
    
def add_expense(amount,category):
    conn=sqlite3.connect("finance.db")
    cursor=conn.cursor()
    
    cursor.execute("""
                   insert into expenses (amount,category) values(?,?)
                   """, (amount,category))
    
    #save
    conn.commit()
    conn.close()
    
    return f"You added:{amount} Euro ({category})"

def get_all_expenses():
    conn=sqlite3.connect("finance.db")
    cursor=conn.cursor()
    cursor.execute("select amount, category from expenses")
    rows=cursor.fetchall()
    
    conn.close()
    
    if not rows:
        return"Rastrat net!"
    
    result="Vse rastratu:\n"
    
    total=0
    for amount, category in rows:
        result += f"- {amount} eur ({category})\n"
        total+=amount
    result+=f"\n Obchie rastratu: {total} evro"
    return result
#DELETE
def delete_expense_by_id(expense_id):
    conn=sqlite3.connect("finance.db")
    cursor=conn.cursor()
    
    cursor.execute("delete from expenses where id=?",(expense_id,))
    
    conn.commit()
    conn.close()
    
    return f"DELETED expense #{expense_id}"
#delete last expense
def delete_last_expense():
    conn=sqlite3.connect("finance.db")
    cursor=conn.cursor()
    
    cursor.execute("""
                   SELECT id
                   FROM expenses
                   ORDER BY id DESC
                   LIMIT 1
                   """)
    
    row=cursor.fetchone()
    
    if not row:
        conn.close()
        return "No expenses"
    
    last_id = row[0]
    
    cursor.execute("delete from expenses where id=?", (last_id,))
    
    conn.commit()
    conn.close()
    
    return f"Deleted last expenses"

#update info

def update_expense(expense_id,new_amount):
    conn=sqlite3.connect("finance.db")
    cursor=conn.cursor()
    
    cursor.execute("update expenses set amount=? where id=?",(new_amount, expense_id))
    
    conn.commit()
    conn.close()
    
    return f"Expense #{expense_id} updated to {new_amount} eur"

    
    
        
