from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI( 
    model="gemini-flash-latest",
    google_api_key="")
   
    
           

def parse_expense(text):
    prompt=f"""
    Dostan iz texsta summu i kategoriu.
    Text:"{text}"
    Otvet v formate:
    amount=...
    category=...
    """
    
    
    
    result = llm.invoke(prompt)
    response = result.content

    if isinstance(response, list):
        parts = []
        for item in response:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and "text" in item:
                parts.append(item["text"])
            else:
                parts.append(str(item))
        response = "\n".join(parts)

    amount = None
    category = None

    for line in response.split("\n"):
        line = line.strip()

        if line.startswith("amount="):
            try:
                amount = int(line.split("=", 1)[1].strip())
            except ValueError:
                amount = None

        elif line.startswith("category="):
            category = line.split("=", 1)[1].strip()

    return amount, category