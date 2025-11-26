from langchain_text_splitters import CharacterTextSplitter

text = "This is a long document with multiple sentences. We need to split it into smaller chunks. This helps with processing large amounts of text."

text_splitter = CharacterTextSplitter(
    separator=".",  # Split by periods
    chunk_size=50,  # Max 50 characters per chunk
    chunk_overlap=10, # 10 characters overlap
    length_function=len
)

chunks = text_splitter.split_text(text)
print(chunks)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")