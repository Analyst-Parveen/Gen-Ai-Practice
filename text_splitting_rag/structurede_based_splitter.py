from langchain_text_splitters import RecursiveCharacterTextSplitter
text='''my name is parveen
i am 25 years old

i live in haryana
how are you.'''

splitter=RecursiveCharacterTextSplitter(
    chunk_size=18,
    chunk_overlap=0,

)
chunk=splitter.split_text(text)
print(len(chunk))
print(chunk)