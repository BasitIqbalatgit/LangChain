# 3 REASONS TO USE PROMPT TEMPLATE INSTEAD OF A SIMPLE STRING.
# 1. Default validation (by using validate_template you wont miss any variable)
# 2. Reusable (by using the .save method you can create a json file and then load it where ever needed)
# 3. Langchain Ecosystem (you can use the chaining concept easily with it)


from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)


template.save('template.json')


