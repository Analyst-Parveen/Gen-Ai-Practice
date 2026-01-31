from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding=HuggingFaceEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2'
)

documents=['''Nobita is a fictional character from the Japanese cartoon Doraemon.
He is known for being lazy but kind-hearted and often needs Doraemon’s help.''',

'''Rohit Sharma is an Indian cricketer famous for his elegant batting style.
He is the captain of the Indian cricket team in limited-overs formats.''',

'''Nobita is a fictional character from the Japanese cartoon Doraemon.
He is known for being lazy but kind-hearted and often needs Doraemon’s help.''',

'''Parveen Sharma is a personal name that can refer to an individual identity.
The name is commonly used in India and may represent a student or professional.''',

'''Football is a popular sport played and watched all over the world.
It involves two teams trying to score goals by kicking a ball.'''
]

query='tell me about parveen sharma'

embed_docs=embedding.embed_documents(documents)
embed_query=embedding.embed_query(query)

score=cosine_similarity([embed_query],embed_docs)[0]


index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(" ")
print(query)
print(documents[index])
print('similarity score is :',score)
