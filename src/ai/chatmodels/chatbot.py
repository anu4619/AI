from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
model = ChatOpenAI(
    model = "gpt-6-luna")
messages=[
    SystemMessage(content="You are a funny assistant"),
]

print("--------------------welcome type 0 to exit the application --------------------")
while True:
    
    prompt = input("You :")
    messages.append(HumanMessage(content=prompt))
    if prompt =="0":
        break
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("AI :",response.content)

print(messages)