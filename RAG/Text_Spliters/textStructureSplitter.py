from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
This is a long document with multiple paragraphs.

Each paragraph discusses a different topic, but they are all related.
The recursive character text splitter is designed to handle such documents effectively.
It will attempt to keep paragraphs together as long as possible.

If a paragraph is too long, it will then split by sentences, and so on.
This ensures that semantic meaning is preserved across chunks.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""] # Default separators can be customized
)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n---")