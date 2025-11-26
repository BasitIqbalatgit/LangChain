# TypeDict is just used to define a dictionary with a specific type for the keys and values, so we can use it to define the type of the dictionary
# it is only for representation and not for the validation of the data meaning we can use it to define the type of the dictionary but we can't use it to validate the data

# Example 1:

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int


user: User ={"name": "Basit Iqbal", "age": 22} # this is valid because the keys and values are of the correct type and if you hover over the user variable you will see the type of the dictionary
# BUT it is not for validation of the data meaning you can add more keys and values to the dictionary and it will not give you an error
# user["email"] = "basit@gmail.com" # this will give you an error because the email key is not in the dictionary
# also if you make the age string it will still not give and error.
user2: User ={"name": "Basit Iqbal", "age": "22"} # this is valid because the age value is a string and not an integer
user3 : User = {}
print(user)
print(user2)
print(user3)



# Types of TypedDict: 
# 1. literal
# 2. Annotation
# 3. Optional
# 4. Complex with pros and cons.