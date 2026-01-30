from chatmodel_hf_api import model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

parser=JsonOutputParser()

template1=PromptTemplate(
    template='Give the name age and city of a fictional persons /n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


# prompt=template1.format()
# # print(prompt)

# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(type(final_result),final_result['name'])



# with chain ------------------------------------------------------------------------------------
chain=template1 | model | parser
result=chain.invoke({})
print(result,type(result))
print(result['name'])