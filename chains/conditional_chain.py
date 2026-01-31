from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text-generation',
    temperature=0

)
model=ChatHuggingFace(llm=llm)
parse=StrOutputParser()

class feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='give the sentimenmt of the feedback')

parse2=PydanticOutputParser(pydantic_object=feedback)    
prompt=PromptTemplate(
    template='classify the sentiment of the following feedback text is negative or positive \n{feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parse2.get_format_instructions()}
)

classifier_chain=prompt|model|parse2

prompt2=PromptTemplate(
    template='write the appropriate response to the positive feedback in sort \n {feedback}',
    input_variables=['feedback']
    )
prompt3=PromptTemplate(
    template='write the appropriate response to the negative feedback in sort \n {feedback}',
    input_variables=['feedback']
    )

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",prompt2|model|parse),
    (lambda x:x.sentiment=='negative',prompt3|model|parse),
    RunnableLambda(lambda x:"could not find sentiment")
)

chain=classifier_chain|branch_chain
result=chain.invoke({
    'feedback':'The phone has poor performance and bad battery life'
})

print(result)
chain.get_graph().print_ascii()