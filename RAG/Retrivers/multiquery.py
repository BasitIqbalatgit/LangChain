# it is used because sometimes the user enters the ambigous query like
# query : How can i stay healty?
# it is vague query instead of entering what should i eat to stay healthy or what should be my exercise routine to stay healthy he asked a vague question so then we would use Multi Query.

# What it will do is that it will give the query to the llm and then the llm will generate 5 to 10 queries and then those queries will search (i.e retrieve data seprately and then the docs fetched by those with the most relevant will be shown to user i.e top 3 or 2 etc)


from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.documents.base import Document
from langchain_classic.retrievers import MultiQueryRetriever


load_dotenv()

# Initialize the embedding and chat models
embd_model = OpenAIEmbeddings()
chat_model = ChatOpenAI()

# Relevant health & wellness documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

# Create the FAISS vector store using the embedding model
vector_store = FAISS.from_documents(
    documents=all_docs,
    embedding=embd_model
)

# Create retrievers
similarity_retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2})

# Create MultiQueryRetriever with the similarity retriever and LLM
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=similarity_retriever,
    llm=chat_model
)

# Test query
query = "How to improve energy levels and maintain balance?"

# Invoke MultiQueryRetriever
result = multiquery_retriever.invoke(query)

# Print results from MultiQueryRetriever
print("MultiQueryRetriever Results:")
for i, doc in enumerate(result):
    print(f"Result {i+1}: {doc.page_content}")
    

# Simple similarity-based retrieval
print("==========================================================")
print("Simple Similarity Result")

result2 = similarity_retriever.invoke(query)
for i, doc in enumerate(result2):
    print(f"Result {i+1}: {doc.page_content}")
    print("\n--------------------------------------------\n")
