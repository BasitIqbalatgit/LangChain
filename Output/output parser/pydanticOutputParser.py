from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

# Schema 
class Person(BaseModel):
    name: str = Field(description="Name of the Person")
    age: int = Field(gt=18, description="Age of the Person")
    city: str = Field(description="City to which the Person Belongs")

# Parser
parser = PydanticOutputParser(pydantic_object=Person)

#model
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# template
template = PromptTemplate(
    template="Generate the name age and city of the person from country {place} \n {format_instr}",
    input_variables=['place'],
    partial_variables={'format_instr': parser.get_format_instructions()}
)

# Make the Prompt
prompt = template.invoke({'place': 'Pakistan'})
result = model.invoke(prompt)
parsed_result= parser.parse(result.content)
print("Parsed Result : ", parsed_result)


# Now Making Chain
chain = template | model | parser
res=chain.invoke({'place':'USA'})
print("After Chaining: ", res)