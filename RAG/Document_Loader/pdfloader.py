from langchain_community.document_loaders import PyPDFLoader

# Ensure you have the necessary libraries installed:
# pip install langchain-community pypdf

# Define the file path (make sure 'machine.pdf' exists in your current directory)
file_path = 'machine.pdf'
loader = PyPDFLoader(file_path)

# --- Original Load Method (Load all at once) ---
print("--- Standard Load Output (List of Document objects) ---")
doc_list = loader.load()

# Printing the whole list will show metadata and snippet of content
print(doc_list)

# If you want to display all text content:
# for document in doc_list:
#     print(document.page_content)


# --- Streaming/Lazy Load Method ---
print("\n--- Lazy Load Output (Streaming page content) ---")

# The variable name 'docs' here is a generator object that yields Document objects one by one
docs_generator = loader.lazy_load()

# Iterate through the generator
# In your original code, you used 'docs' and 'doc' confusingly inside the loop.
for document in docs_generator:
    # 'document' is a single Document object yielded by the generator
    # We access its text content via the attribute '.page_content'
    # We slice it to the first 100 characters for a snippet preview
    print(document.page_content[:100] + "...") # Added '...' for visual indication of snippet
    print("-" * 20) # Add a separator between pages for clarity

