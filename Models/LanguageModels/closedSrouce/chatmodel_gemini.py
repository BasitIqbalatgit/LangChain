from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Using gemini-2.5-flash which is available in the API
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

result = model.invoke("what is the capital of Pakistan?")
print("Result is:", result.content)