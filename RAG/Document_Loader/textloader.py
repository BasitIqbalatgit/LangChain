from langchain_community.document_loaders import TextLoader

# Initialize the TextLoader with the path to your text file
loader = TextLoader("abc.txt")

# Load the documents
documents = loader.load()

# 'documents' will be a list of Document objects
# Each Document object will have 'page_content' and 'metadata'
for doc in documents:
    print(f"Page Content: {doc.page_content[:100]}...") # Print first 100 chars
    print(f"Metadata: {doc.metadata}")