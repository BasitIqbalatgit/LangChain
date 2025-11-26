from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

#Scenerio : topic -> LLm (chatopenai) -> detailed report -> LLM(google gemini) -> 5 line summary

prompt1 = PromptTemplate(
    template="""Generate a Detailed Report about the topic -> {topic}""",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="""Sumarize this detailed Report into 5 POINTS -> {report} """,
    input_variables=['report']
)


model1 = ChatOpenAI()
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

result = chain.invoke({'topic': 'NLP'})

print("RESULT: ", result)


print("\n\n\n GRAPH \n\n ")
chain.get_graph().print_ascii()