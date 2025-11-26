# importing
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
#load env
load_dotenv()
# schema using pydantic
class Review(BaseModel):
    name: str = "Guest"
    age : Optional[int] = Field(default=18,description="Select the age of the user from the review.")
    


# model

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
structured_model =model.with_structured_output(Review)
prompt= """i have used iphone 11. I liked its Style , camera and display. written by Basit Iqbal"""

#getting response and playing with it.


response = structured_model.invoke(prompt)

print("Response is : ", response)