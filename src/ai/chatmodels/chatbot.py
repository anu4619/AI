from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
model = ChatOpenAI(
    model = "gpt-6-luna")
print("choose your AI mode")
print("1. funny mode")
print("2. serious mode")
print("3. sarcastic mode")
print("4. angry mode")
choice=int(input("Enter your choice: "))
if choice == 1:
    mode="You are a funny assistant. respond with humor and jokes"
elif choice == 2:
    mode="You are a serious assistant.keep your tone serious and straight forward"
elif choice == 3:
    mode="You are a sarcastic assistant. respond with sarcasm and witty remarks"
elif choice == 4:
    mode="You are an angry assistant. respond with anger and frustration"
messages=[
    SystemMessage(content=mode),
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