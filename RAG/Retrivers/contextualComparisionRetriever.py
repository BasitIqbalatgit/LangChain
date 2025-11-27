from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents.base import Document
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

load_dotenv()

# Recreate the document objects from the previous data
docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]


embedding_model = OpenAIEmbeddings()
chat_model = ChatOpenAI()

vector_store = FAISS.from_documents(
    documents = docs,
    embedding=embedding_model
)

# base _ retriver
base_retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})

#base_compressor
# base_compressor = LLMChainExtractor(llm=chat_model)
llm = ChatOpenAI(model="gpt-3.5-turbo")
base_compressor = LLMChainExtractor.from_llm(llm)

contextual_compress_retriever = ContextualCompressionRetriever(
base_retriever = base_retriever,
base_compressor= base_compressor
)


# Query the retriever
query = "What is photosynthesis?"
compressed_results = contextual_compress_retriever.invoke(query)


for i,doc in enumerate(compressed_results):
    print(f"Result {i+1}: {doc.page_content} \n")