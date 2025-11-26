#Scenerio : topic-> LLM -> [Detailed Report] -> LLM -> 5 line summary

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Load environment variables
load_dotenv()


# Initialize the OpenAI model (using langchain_openai)
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# template 1
template1 = PromptTemplate(
    template="The topic for which you have to Generarte the Detailed Report is : {topic}",
    input_variables = ['topic']
)

# template 2
template2 = PromptTemplate(
    template = "You have to Generate a 5 line summary for this {text}",
    input_variables= ['text']
)

# Using Parser.
parser = StrOutputParser()

# Making the chain
chain = template1 | llm | parser | template2 | llm | parser

response = chain.invoke({'topic': 'Ai Engineering'})
# response to playwith
print("RESPONSE : ", response)
