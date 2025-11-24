from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text= "Hello, world!"
document=["Basit Iqbal", "Ahsan Iqbal", "Hasnain Iqbal", "Manahil Iqbal", "Munaza Iqbal"]

print(embeddings.embed_query(text))
# print(embeddings.embed_documents(document))