from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough


load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1= PromptTemplate(
    template="""Generate a Summary on this Topic : {topic}""",
    input_variables=['topic']
)

gen_summary = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>100, gen_summary),
    RunnablePassthrough()
)

main_chain = RunnableSequence(gen_summary, branch_chain)

response = main_chain.invoke({'topic': 'Ai'})
print(response)

main_chain.get_graph().print_ascii()