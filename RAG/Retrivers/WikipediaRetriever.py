from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang='en')

query="The GeoGraphical history of Pakistan and India from the perspective of China"

docs= retriever.invoke(query)

for i ,  doc in enumerate(docs):
    print(f"Result {i+1}: {doc.page_content}")