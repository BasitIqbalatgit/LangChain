from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough



load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1= PromptTemplate(
    template="""Generate a joke out of this prompt : {promp}""",
    input_variables=['promp']
)

prompt2=PromptTemplate(
    template="""Generate the explanation for this joke : {joke}""",
    input_variables=['joke']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt2,model,parser)
    }
)

combined_chain = RunnableSequence(joke_gen_chain, parallel_chain)

response = combined_chain.invoke({'promp': "AI"})
print(response)