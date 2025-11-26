from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatOpenAI()

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="""Generate a joke on this Topic : {topic}""",
    input_variables=['topic']
)

def word_count(x):
    return len(x.split())


gen_joke= RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
})

# same thing with lambda func
# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'word_count' : RunnableLambda(lambda x : len(x.split()))
# })


main_chain= RunnableSequence(gen_joke,parallel_chain)

response = main_chain.invoke({'topic': 'Cricket'})

print(response)
formated_result = """{} \n word count : {}""".format(response['joke'], response['word_count'])
print(formated_result)