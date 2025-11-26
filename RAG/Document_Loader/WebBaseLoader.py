from langchain_community.document_loaders import WebBaseLoader


url="https://github.com/campusx-official/langchain-chains/blob/main/conditional_chain.py"
loader =  WebBaseLoader(url)

document = loader.load()

print(document)