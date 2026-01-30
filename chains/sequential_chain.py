from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text-generation'

)
model=ChatHuggingFace(llm=llm)
parse=StrOutputParser()

prompt1=PromptTemplate(
    template='explain a 100 line paragraphs on the following topic \n {topic}',
    input_variables=['topic']

)

prompt2=PromptTemplate(
    template='give the 10 important keywords from the following paragraphs \n {text}',
    input_variables=['text']
)

chain=prompt1|model|parse|prompt2|model|parse
result=chain.invoke({
    'topic':'Honesty Is The Best Policy'
})

print(result)

chain.get_graph().print_ascii()