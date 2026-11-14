from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    model = "gpt-6-luna")
messages=[]

print("--------------------welcome type 0 to exit the application --------------------")
while True:
    
    prompt = input("You :")
    messages.append(prompt)
    if prompt =="0":
        break
    response=model.invoke(messages)
    messages.append(response.content)
    print("AI :",response.content)

print(messages)