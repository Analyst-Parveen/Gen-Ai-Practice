from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)
result=model.invoke('who is the prime minister of india')
print(result.content)