from model_loder import model
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# chat_template=ChatPromptTemplate([
#     SystemMessage(content='you are a helpful {domain} expert '),  # not work use tupple method writeen as below
#     HumanMessage(content='tell me who is {query}')

# ])

chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert '),
    ('human','tell me who is {query}')

])

prompt=chat_template.invoke({
    'domain':"AI expert",
    'query':'Narender modi'
})

print(prompt)
