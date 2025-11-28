from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.tools import tool
load_dotenv()
summarizer = create_agent(
    model='gpt-4o-mini',
    tools=[],
    system_prompt=(
        "You are a summarizer agent. "
        "Given raw text (possibly long, from multiple sources), "
        "produce a concise, clear summary. "
        "Focus on main points, highlight key facts, and make the summary readable."
    )
)


@tool
def summarize(text: str)->str:
    """This tool will take the text and summarize it and then return it"""
    result = summarizer.invoke({
        'messages':[
            {'role':'user', 'content':text}
        ]
    })
    
    return result['messages'][-1].content



