from db import init_db
from agent import agent

init_db()


while True:
    
    text=input("input >> ")
    if text =="exit":
        break
    
    print(agent(text))
    