from langchain_huggingface import HuggingFaceEmbeddings,HuggingFacePipeline

embedding=HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2')

text=['delhi is the capital of india',
      'parveen is the name of king',
      'cricket is a game played by mens',
      'holy is the festival of colors']

vector=embedding.embed_documents(text)

print(vector)
