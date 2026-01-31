from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path=r'C:\Users\PC-032\Desktop\Langchain_models\document_loader\directory',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
print(len(docs))
print(docs)