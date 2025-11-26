from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from  dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()
#                            --> LLM for summary --
#Scenerio : Detailed Report  |                     |--> LLM for meging --> a new Document
#                            --> LLM for quiz    --    


#   -------------------------------------PROMPTS-----------------------------------                           
prompt1= PromptTemplate(
    template="""Generate a Short and Concise Summary for this text : {text}""",
    input_variables= ['text']
)
prompt2= PromptTemplate(
    template="""Generate the 5 Question Quiz from this text -> {text}""",
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template="""Merge both the summary -> {notes} and the quiz -> {quiz}""",
    input_variables=['notes', 'quiz']
)

#------------------------------------MODELS----------------------------------------------
model1= ChatOpenAI()
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


#---------------------------------------PARSER---------------------------------
strParser = StrOutputParser()

# To Make Parallel Chains you have to use RunnableParallel from langchain.core.runnable
# chain1 = prompt1 | model1 | strParser
# chain2 = prompt2 | model2 | strParser
# This would be a sequential way not parallel so now using Parallel

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | model1 | strParser,
        'quiz' : prompt2 | model2 | strParser
    }
)

merged_chain = prompt3 | model2 | strParser

chain = parallel_chain | merged_chain

txt = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.

"""

result = chain.invoke({'text': txt})

print(result)