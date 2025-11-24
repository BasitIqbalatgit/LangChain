from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational",
)


print(llm.invoke("What is the capital of Pakistan?"))


# Your code	HF endpoint used	Model supports it?	Result
# ChatHuggingFace → invoke()	conversational	YES	works
# HuggingFaceEndpoint → invoke()	text-generation	NO	fails


