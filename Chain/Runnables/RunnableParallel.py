from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

prompt1=PromptTemplate(
    template="""Generate A Tweet Post for this topic : {topic}""",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="""Generate a Linkedin Post for this topic : {topic}""",
    input_variables=['topic']
)

parser = StrOutputParser()

model = ChatOpenAI()

parallel_chain = RunnableParallel({
    'tweet' : prompt1 | model | parser,
    'linkedin' : prompt2 | model | parser
})

response = parallel_chain.invoke({'topic': 'Ai'})
print(response)