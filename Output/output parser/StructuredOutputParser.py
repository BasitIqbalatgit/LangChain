from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

# Load .env from the Output directory
load_dotenv()

# define schema
schema = [
    ResponseSchema(name="fact1", description="Fact 1 about topic"),
    ResponseSchema(name="fact2", description="Fact 2 about topic"),
    ResponseSchema(name="fact3", description="Fact 3 about topic"),
]

# create parser
parser = StructuredOutputParser.from_response_schemas(schema)

# build prompt template
template = PromptTemplate(
    template="Give me facts about {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# initialize model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# format the prompt
prompt_str = template.format(topic="AI and ML")

# call the model
response = model.invoke(prompt_str)  

# parse the content (assuming .content holds the text)
parsed = parser.parse(response.content)

print("PARSED RESULT:", parsed)
