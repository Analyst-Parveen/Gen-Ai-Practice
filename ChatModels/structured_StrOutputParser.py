from chatmodel_hf_api import model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1st prompt script--
template1=PromptTemplate(
    template='write a detailed report on {report}',
    input_variables={'report'}
)

# 2nd prompts----------------
template2=PromptTemplate(
    template='explain the five line summary on the following text /n {text}',
    input_variables=['text']

)

# prompt1=template1.invoke({
#     'report':'blackhole'
# })

# result1=model.invoke(prompt1)

# prompt2=template2.invoke({
#     'text':result1.content
# })

# result2=model.invoke(prompt2)

# print(result2.content)

#------------------------------ with StrOutput parse  methods

parse=StrOutputParser()

chain=template1 | model | parse | template2 | model |parse 

result=chain.invoke({
    'report':'India'
})

print(result)