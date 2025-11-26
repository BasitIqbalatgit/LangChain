# imports
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# load envs
load_dotenv()

# schema
json_schema = {
    "title": "Review",
    "description": "This Schema is of the Reivew of the Products of Amazon",
    "type": "object",
    "properties":{
        "key_theme":{
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List down all the key themes present in the review. "

        },
        "summary":{
            "type": "string",
            "description":"Write a 2 line summary of the review"
        },
        "sentiment":{
            "type": "string",
            "enum" : ["pos", "neg"],
            "description": "Write the sentiment of the review."
        },
        "name":{
            "type": ["string", "null"],
            "description": "Extract the name of the reviewer."
        },
        "pros":{
            "type": ["array", "null"],
            "items" :{
                "type" : "string"
            },
            "description": "Extract the Pros (i.e advantages from the review.)"
        }
    },
    "required": ["key_theme", "summary", "sentiment"]
}

#model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
struct_model = model.with_structured_output(json_schema)


# Prompt
prompt = """
Review Title: My Experience with the Acme 4K Monitor

I recently purchased the Acme 4K Monitor from Amazon seller 'TechDealz' after much deliberation. Overall, I am reasonably happy with the purchase, but there are some glaring issues that prevent me from giving it 5 stars. The picture quality is simply stunning; the 4K resolution paired with the vibrant colors makes gaming and movie watching a joy. The slim bezel design is very modern and looks great on my desk.

However, the built-in speakers are abysmal. They sound tinny and low-volume, so I immediately had to connect external speakers (which defeats the minimalist purpose). Also, the stand is incredibly wobbly. The monitor shakes every time I type slightly fast.

It was delivered on time and packaged well. Signed, A Satisfied Customer, James R.
"""
# Response

response = struct_model.invoke(prompt)

print("Response : ", response)


