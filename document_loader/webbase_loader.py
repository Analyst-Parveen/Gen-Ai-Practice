from langchain_community.document_loaders import WebBaseLoader,SeleniumURLLoader
from model import model,parser
from langchain_core.prompts import PromptTemplate

url='https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509?pid=COMH9ZWQCJGMZGXE&lid=LSTCOMH9ZWQCJGMZGXEBSSIQU&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=f3eb2a5a-282e-4c19-8035-66f14f087547.COMH9ZWQCJGMZGXE.SEARCH&ppt=None&ppn=None&ssid=0p1uuhi8xs0000001768236489314'


loader=WebBaseLoader(url)
docs=loader.load()
# print(len(docs))
# print(docs[0].page_content)
model=model
parser=parser

prompt=PromptTemplate(
    template='answer the following question {question}  from the following text {text}',
    input_variables=['question','text']
)

chain=prompt|model|parser

result=chain.invoke({
    'question':"What is the price of product",

    'text':docs[0].page_content

})
print(result)