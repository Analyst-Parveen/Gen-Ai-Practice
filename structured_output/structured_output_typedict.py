
# from typing import TypedDict
# class person(TypedDict):
#     name:str
#     age:int

# new_person:person={
#     'name':'parveen',
#     'age':35
# }

# print(new_person)

#------------------------------------------------------------------------------------------------------------------

from model_loder1 import model
from typing import TypedDict

class Review(TypedDict):
    summary:str
    sentiment:str

structered_output=model.with_structured_output(Review)

result=structered_output.invoke('I have been using this online learning platform for the past three months, and overall it has been a good experience. The course content is well-structured and easy to follow, especially for beginners. The instructors explain concepts clearly with practical examples, which makes learning more effective.')

print(result)