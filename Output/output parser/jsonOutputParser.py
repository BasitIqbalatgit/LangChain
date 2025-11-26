from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

#parser
parser = JsonOutputParser()

# tempalte
template = PromptTemplate(
    template= "Give me the data for a fictional Anime Character name,age,anime in which he was \n {format_instructions}",
    input_variables =[],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

# model
# model = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash')
model = ChatOpenAI()

# before chain
prompt = template.format()
response = model.invoke(prompt)
parsedResponse = parser.parse(response.content)
print(parsedResponse)

