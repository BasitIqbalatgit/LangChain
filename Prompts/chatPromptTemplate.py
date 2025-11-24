# ChatPromptTemplate: it is a little differnt from PromptTemplate as it is used for multi-turn-conversation while PromptTemplate is used for single turn conversation.
# for ChatPrompTemplate remember these points:
# 1. import it from langchain_core.prompts
# 2. you have to pass it the array of Messages in 'tuple'form.


from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are an expert in the field of {domain}'),
    ('human', 'Explain in simple terms what is {topic}')
])

prompt = chat_template.invoke({'domain': 'Ai Engineering', 'topic': 'Embeddings'})
print("Prompt : ", prompt)