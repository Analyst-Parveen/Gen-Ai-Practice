from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(r'C:\Users\PC-032\Desktop\Langchain_models\document_loader\regression_dataset.csv')
docs=loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[5])
