from langchain_core.documents.base import Document
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma

load_dotenv()


# Create LangChain documents for IPL players

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )


docs =[doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    embedding_function = OpenAIEmbeddings(),
    persist_directory = 'my_chroma_db',
    collection_name = 'sample'
)

# adding Docs
vector_store.add_documents(docs)

#View Documents
Docu = vector_store.get(include=['embeddings', 'documents', 'metadatas'])
print(Docu)

# Update Docs
new_doc = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata ={"team": "Royal Challengers Bangalore"}
)
vector_store.update_document(document_id="53e03eef-464e-4913-9ced-338e3270282c", document=new_doc)

# deleted Doc
vector_store.delete(ids=['9c7540cc-1f4a-48d6-86b5-e61ad1f4ad50'])

# Search document
simple_search= vector_store.similarity_search(
    query="Who is the best Bowler",
    k=2 # specify the number of docs you want
)
print("Simple Search is : ", simple_search)

print("\n\n\n")
# searh document with similarity Score
search_with_score = vector_store.similarity_search_with_score(
    query="Who is the best bowler",
    k=2
)

print("Similarity Search with score is : ", search_with_score)

print("\n\n\n")

# Meta Data Filtering
filtered_results= vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Royal Challengers Bangalore"}
)
print("Filtered Result is : ",len(filtered_results) , " and " ,filtered_results)


