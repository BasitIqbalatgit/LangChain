from langchain.agents import create_agent
from tools import web_search, load_web_page
from langchain_core.tools import tool
from dotenv import load_dotenv
load_dotenv()

# Creating the researcher agent using the two tools
researcher_agent = create_agent(
    model="gpt-4o-mini",  # Ensure you are using a valid model name
    tools=[web_search, load_web_page],
    system_prompt=(
        "You are a researcher agent. "
        "Given a user topic, you will use the web_search tool to find relevant URLs, "
        "then use load_web_page to fetch full content, "
        "and return a combined raw text covering multiple sources."
    )
)

# Define a tool to interact with the agent
@tool
def research(query: str):
    """This tool invokes the researcher agent to perform a search and return content."""
    # Pass the query as a user message to the agent
    result = researcher_agent.invoke({
        'messages': [
            {'role': 'user', 'content': query}
        ]
    })
      
    
    return  result['messages'][-1].content 


