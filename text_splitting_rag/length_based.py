from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(r'C:\Users\PC-032\Desktop\Langchain_models\text_splitting_rag\Abhinav_Sharma_RUC.pdf')
docs=loader.load()
# print(len(docs))

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_text(docs[12].page_content) # to split a particular page or a particular object
print(len(result))
print(result)



# result=splitter.split_documents(docs)  # to split whole documents-----------
# print(len(result))
# print(result)