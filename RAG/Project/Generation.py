from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv
from Augmentation import fullPrompt, format_docs

load_dotenv()

def create_rag_chain(retriever):
    """
    Create a complete RAG chain with retriever, prompt, and model.
    
    Args:
        retriever: MMRRetriever instance for document retrieval
    
    Returns:
        chain: A LangChain Runnable chain for RAG
    """
    # Initialize the model
    model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
    
    parser = StrOutputParser()
    
    # Create the prompt template
    prompt = fullPrompt(context="{context}", question="{question}")
    
    parallel_chain= RunnableParallel({
        'context': lambda x: format_docs(retriever.mmr_retrieve(x['question'])),
        'question': RunnablePassthrough()
    })
    
    fullChain = parallel_chain | prompt | model | parser
    
    return fullChain

def generate_response(retriever, question):
    """
    Generate a response to a question using the RAG chain.
    
    Args:
        retriever: MMRRetriever instance
        question: User's question
    
    Returns:
        str: Generated response
    """
    chain = create_rag_chain(retriever)
    response = chain.invoke({"question": question})
    return response
