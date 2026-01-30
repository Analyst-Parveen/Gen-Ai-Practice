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

prompt=PromptTemplate(
    template='generate five interesting facts about {topic}',
    input_variables=['topic']
)

parse=StrOutputParser()

chain= prompt|model|parse

result=chain.invoke({'topic':'cricket'})
print(result)
chain.get_graph().print_ascii()