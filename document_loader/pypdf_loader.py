from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(r'C:\Users\PC-032\Desktop\Langchain_models\document_loader\Abhinav_Sharma_RUC.pdf')
# docs=loader.load()
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
# print(docs)

# for document in docs:
#     print(document.metadata)


docs1=loader.lazy_load()

for document in docs1:
    print(document.page_content)