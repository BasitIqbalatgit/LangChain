from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    repo_id= "sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
)

print(embeddings.embed_query("Hello, world!"))
# print(embeddings.embed_documents(["Hello, world!", "Hello, world!", "Basit Iqbal", "Ahsan Iqbal", "Hasnain Iqbal", "Manahil Iqbal", "Munaza Iqbal"]))