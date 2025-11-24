# MessagePlaceholder: in langchain is a special placeholder used inside the ChatPromptTemplate to dynamically insert chat history or a list of messages at run time
# Purpose: now consider a scenerio that a customer at amazon had a chat with the Ai agent one day in a particular session and then next day he can back and created a new Chat session and asked for the previous data as in the example below then we have to provide the chat_history as a placeholder before hand so that the agent knows what to answer.(i.e so that agent has the context)


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful ai assistant for amazon'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

#load history : you can load it from db, files etc i am just going to write it here for now as i have loaded it in his and appending it to chat_history
chat_history=[]
with open('data.txt') as f:
    chat_history.extend(f.readlines())

# create prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query': "Why havent i got the refund Yet?"})
print("PROMPT : ", prompt)