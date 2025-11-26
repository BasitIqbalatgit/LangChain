# pydantic : is a data validation and data parsing library for python. it ensures that the data you work with is correct, structured and tpye safe
# it is used for:
# 1. data validation        2. default_values    3. automatic type conversion

from pydantic import BaseModel, Field
from typing import Literal, Optional

class Student(BaseModel):
    name: str  # simple 
    age : int = None # default value
    sentiment : Literal['pos' , 'neg']  # if i give something other then this it will raise an error.
    # Optional Fields
    pros : Optional[list[str]] = Field(default= None, description="List down the Pros of the review.")
    cons  : Optional[list[str]] = Field(description="List Down the Cons of the Review") # when default is not written it considers it Required .




# Coerce : implicit type casting:
new_std = {'name': 'Basit Iqbal', 'age':22, 'sentiment': 'pos', 'cons':['bad']}


# * -> for positional arguments passing (when passed to a function) and collection (in the parameter of the function)
# ** -> for keyword arguments passing and collection.

std = Student(**new_std)

print(type(std))
print(std)

print(dict(std)["name"]) # can convert to dict 
print(std.model_dump_json())
