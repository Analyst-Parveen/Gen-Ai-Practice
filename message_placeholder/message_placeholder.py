from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat template
chat_template=ChatPromptTemplate([
    ('system','you are a helpful customersupport agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')

])

chat_history=[]
# load chat history
with open ('message_placeholder/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt
prompt=chat_template.invoke({
    'query':'where is my refund',
    'chat_history':chat_history
})    

print(prompt)