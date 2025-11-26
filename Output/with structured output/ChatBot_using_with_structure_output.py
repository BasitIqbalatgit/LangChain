# Use the working Google integration instead
from langchain_google_genai import ChatGoogleGenerativeAI 
from pydantic import BaseModel, Field # Pydantic often works better than TypedDict with robust APIs
from typing import Literal, Optional
from dotenv import load_dotenv

load_dotenv()
# Define schema using Pydantic
class ReviewSchema(BaseModel):
    summary: str = Field(description="simple summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="return sentiment of the review")
    confidence: float = Field(description="return confidence of the sentiment")
    reasoning: Optional[str] = Field(description="Explanation for the sentiment")

llm_google = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
structured_model_google = llm_google.with_structured_output(ReviewSchema)

prompt = """laptop is very easy to use and it is very fast and it is very good."""
response = structured_model_google.invoke(prompt)

print("Type of response: ", type(response))
print("Response: ", response)
print("Summary:", response.summary)
