from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents.base import Document

load_dotenv()

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step2 : initialize the Embedding model 
embd_model = OpenAIEmbeddings()

# Step3: Create Chroma Vector Store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding = embd_model,
    collection_name= 'my_coll'
)

#Step4: Convert Vector Store into a Retriever 
retriever= vectorstore.as_retriever(search_kwargs={'k': 2})

#Step 5 : Query and Result
query = "What is Chroma used for ?"
result = retriever.invoke(query)


for i,doc in enumerate(result):
    print(f"Result {i+1} : {doc.page_content}")
    print("\n\n ---------------------------------------------------------------\n\n")

    