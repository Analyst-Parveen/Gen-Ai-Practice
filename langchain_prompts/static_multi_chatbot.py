from model_loder import model
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

chat_history=[
    SystemMessage(content="you are a helpful AI assistent")
]
while True:
    user_input=input("you: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI : ',result.content)
    
print(chat_history)    
