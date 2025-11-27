# Now here i will make the retriever to fetch the data from the vectorStore

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

class MMRRetriever:
    def __init__(self, faiss_index_path, lambda_mmr=0.5):
        """
        Initialize the retriever with the FAISS index and MMR lambda parameter.

        Args:
        - faiss_index_path: Path to the saved FAISS index.
        - lambda_mmr: Controls the balance between relevance and diversity (0.5 is a typical starting point).
        """
        self.lambda_mmr = lambda_mmr
        self.vector_store = FAISS.load_local(
            faiss_index_path, 
            OpenAIEmbeddings(),
            allow_dangerous_deserialization=True
        )

    def mmr_retrieve(self, query, top_k=5, fetch_k=20):
        """
        Perform MMR-based retrieval from the FAISS index using FAISS's built-in MMR support.

        Args:
        - query: The query string.
        - top_k: The number of top documents to retrieve.
        - fetch_k: The number of documents to fetch before applying MMR (should be > top_k).

        Returns:
        - selected_docs: The documents selected based on MMR.
        """
        # Use FAISS's built-in max_marginal_relevance_search method
        # This method implements MMR internally with proper diversity handling
        selected_docs = self.vector_store.max_marginal_relevance_search(
            query=query,
            k=top_k,
            fetch_k=fetch_k,
            lambda_mult=self.lambda_mmr
        )
        
        return selected_docs
