from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from  langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="""
Give me the name of the peron who got first position in the batch of FA21 who graduated in Software Engineering from {uni}
""",
input_variables=['uni']
)

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash')

parser = StrOutputParser()


chain = prompt | model | parser

result = chain.invoke({'uni': "COMSATS University Islamabad Abbottabad Campus"})

print("Toper : ", result)