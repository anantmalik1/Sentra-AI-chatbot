from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


model = ChatMistralAI(model="mistral-small-latest",temperature=0.9,max_tokens=20)

print("choose your AI mode")
print("press 1 for Angry mode")
print("press 2 for For Funny mode ")
print("press 3 for sad mode")

choice = int(input("tell your response :-"))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a funny AI agent. You respond with humor and jokes."
elif choice ==3:
    mode = "You are a sad AI agent. You respond with empathy and understanding."


messages = [
      SystemMessage(content="mode") 
      
]
while True:
    print("------------------welcome to the chatbot------------------")
    print("Enter '0' to exit the application")

    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot : ",response.content)