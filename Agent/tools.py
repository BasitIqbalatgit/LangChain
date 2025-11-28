from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

# 1. Web search tool
@tool
def web_search(query: str) -> str:
    """This tool is used to perform a web search; it takes a user query and returns raw text from the web."""
    
    # Initialize DuckDuckGo search
    search = DuckDuckGoSearchRun()
    # Invoke the search and return the results (assuming it returns raw text or relevant links)
    return search.invoke(query)  # Make sure DuckDuckGoSearchRun is implemented to return the raw text

# 2. Scrape tool
@tool
def load_web_page(url: str) -> str:
    """This tool loads the entire HTML page content from a URL and converts it into a Document."""
    
    # Initialize the WebBaseLoader with the given URL
    loader = WebBaseLoader([url])
    # Load the page content (returns a list of documents)
    result = loader.load()
    
    # Assuming the first document contains the full page content
    return result[0].page_content  # Return the actual page content of the first document
