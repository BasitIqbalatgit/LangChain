from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1= PromptTemplate(
    template="""Generate a joke from this topic -> {topic}""",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="""Generate an explanation for this Joke -> {joke}""",
    input_variables=['joke']
)

parser = StrOutputParser()

sequential_chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
response=sequential_chain.invoke({'topic':'Cricket'})
print(response)