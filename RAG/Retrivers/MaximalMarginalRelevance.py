# MMR : Maximal Marginal Relevance.
# search for result that are related to query but diverse from each other
# MMR picks the most relevant document first and then picking the nesxt most similar doc that is least similar to the already selected doc and so on 
# Diversity depends upon the value of lambda_mult  (0 - 1)  ... 0 means diverse and 1 means close

from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.documents.base import Document
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# Step 1: embedding models and documents: 
model = OpenAIEmbeddings()
# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

#Step 2: Making VectorStore
vector_store = FAISS.from_documents(
    documents = docs,
    embedding=model,
)

# Step 3: making a retriever MMR.
mmr_retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={'k':3, 'lambda_mult': 0.5}
)

# Query and Result
query = "What is langchain?"
result = mmr_retriever.invoke(query)


for i,doc in enumerate(result):
    print(f"Result {i+1}: {doc.page_content}")
    print("\n---------------------------------\n")

