from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

print(embeddings.embed_query("Hello, world!"))
documents =["Hello, world!", "Hello, world!", "Basit Iqbal", "Ahsan Iqbal", "Hasnain Iqbal", "Manahil Iqbal", "Munaza Iqbal"]
print(embeddings.embed_documents(documents))
