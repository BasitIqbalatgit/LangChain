# now here i have to make the Augmentation

from langchain_core.prompts import PromptTemplate

def fullPrompt(context, question):
    """
    Create a prompt with context and question.
    
    Args:
        context: Retrieved context from the vector store
        question: User's question
    
    Returns:
        PromptTemplate: The prompt template with context and question
    """
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
         Question: {question}
        """,
        input_variables=['context', 'question']
    )
    
    return prompt

def format_docs(docs):
    """
    Format retrieved documents into a single context string.
    
    Args:
        docs: List of retrieved documents
    
    Returns:
        str: Formatted context string
    """
    return "\n\n".join([doc.page_content for doc in docs])
