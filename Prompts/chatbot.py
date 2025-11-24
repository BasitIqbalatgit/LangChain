from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational",
)
model = ChatHuggingFace(llm=llm)

chat_history=[]
chat_history.append(SystemMessage(content="You are a Great Methamatician who give consise to the point answer in 1 line"))

while True:
    prompt = input("Human: ")
    chat_history.append(HumanMessage(content=prompt))
    if prompt == 'exit':
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI : " , response.content)


print("CHAT HISTORY : ", chat_history)