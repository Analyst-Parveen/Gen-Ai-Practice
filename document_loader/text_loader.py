from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from model import model,parser
text=TextLoader(r'C:\Users\PC-032\Desktop\Langchain_models\document_loader\text.txt',encoding='utf-8')
docs=text.load()
# print(len(docs))
# print(type(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)


prompt=PromptTemplate(
    template="summarize this text in 3  line {text} ",
    input_variables=['text']
)

parser=parser
model=model
chain=prompt|model|parser
summary=chain.invoke({'text':docs[0].page_content})
print(summary)