from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    path='fold',
    glob='*.pdf'

)

documents = loader.load()

print(documents)