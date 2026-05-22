from langchain_google_genai import ChatGoogleGenerativeAI
from tools import add_expense_tool, get_all_expenses_tool, delete_expense_tool,update_expense_tool
llm=ChatGoogleGenerativeAI( 
    model="gemini-flash-latest",
    google_api_key="")

def agent(user_input):
    #!!!!-додай витрату 250 грн на їжу
    if "pocashu vse rastratu" in user_input or "vse rastratu" in user_input:
        return get_all_expenses_tool()
    
    if "udali" in user_input or "delete" in user_input:
        return delete_expense_tool(user_input)
    
    if "change" in user_input or "zemeni" in user_input:
        return update_expense_tool(user_input)
    #dobav rastratu 20 evro za komp muschku
    if "dobav" in user_input or "rastrat" in user_input:
        return add_expense_tool(user_input)
    
    return llm.invoke(user_input).content
    

    