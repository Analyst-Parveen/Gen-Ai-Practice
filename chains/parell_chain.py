from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text-generation'

)
model=ChatHuggingFace(llm=llm)
parse=StrOutputParser()

prompt1=PromptTemplate(
    template='Generate simple and sort notes from the following text \n {text}',
    input_variables=['text']
    
)

prompt2=PromptTemplate(
    template='Generate the 5 quiz or sort question and answer   from the following text \n{text} ',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='Generate a combine document by merging both notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parellel_chain=RunnableParallel({
    'notes':prompt1|model|parse,
    'quiz':prompt2|model|parse
})

merge_chain=prompt3|model|parse

chain=parellel_chain|merge_chain


text='''Linear Regression is one of the most fundamental and widely used algorithms in machine learning and statistics, primarily applied to predict continuous numerical outcomes by modeling the relationship between one dependent variable and one or more independent variables. At its core, linear regression assumes that this relationship can be represented by a straight line, where changes in the input variables lead to proportional changes in the output variable. The model works by fitting a line (or hyperplane in higher dimensions) that best represents the underlying trend in the data, such that the difference between the actual values and the predicted values is minimized. This difference is called the error or residual, and linear regression typically minimizes the sum of squared residuals, a method known as Ordinary Least Squares (OLS). By squaring the errors, the model penalizes larger mistakes more heavily, ensuring that the fitted line is as close as possible to most data points.

Mathematically, linear regression expresses the target variable as a weighted sum of input features plus a bias term. In simple linear regression, where there is only one feature, the equation takes the form 
𝑦
=
𝑚
𝑥
+
𝑐
y=mx+c, where 
𝑚
m represents the slope of the line (indicating how much the output changes for a unit change in the input) and 
𝑐
c is the intercept (the value of the output when the input is zero). In multiple linear regression, this concept extends to several features, each having its own coefficient, allowing the model to capture the combined effect of multiple variables on the target. These coefficients are not chosen arbitrarily; instead, they are learned from data using optimization techniques such as the normal equation or gradient descent. The normal equation provides a direct mathematical solution and works well for smaller datasets, while gradient descent is an iterative approach that is more suitable for large-scale data and real-world machine learning systems.

Linear regression relies on several important assumptions to perform well, including linearity between features and the target, independence of observations, constant variance of errors (homoscedasticity), normal distribution of residuals, and low multicollinearity among input features. When these assumptions are reasonably satisfied, linear regression provides highly interpretable results, making it easy to understand how each feature influences the prediction. This interpretability is one of its biggest strengths and is why linear regression is extensively used in domains such as economics, finance, healthcare, and social sciences. Despite its simplicity, linear regression forms the foundation for many advanced machine learning models and concepts, such as regularization (Ridge and Lasso), generalized linear models, and even neural networks, making it an essential algorithm for anyone learning data science or machine learning.'''
result=chain.invoke({
    'text':text
})

print(result)

chain.get_graph().print_ascii()