from langchain.agents import create_agent
from researcher import research
from summarizer import summarize
from dotenv import load_dotenv

load_dotenv()
orchestrator = create_agent(
    model='gpt-4o-mini',
    tools=[research, summarize],
    system_prompt=(
        "You are a supervisor agent. "
        "When the user gives a request, you decide whether to first call research_topic (to gather data), "
        "and then call summarize_text (to produce final answer). "
        "Return the final output to the user. "
        "You may call both tools in sequence when needed."
    )
)


def run ():
    user_input = input("What do you want to learn about ?")
    resp = orchestrator.invoke({
        'messages':[
            {'role':'user', 'content': user_input}
        ]
    })
    
    print("Answer: ", resp['messages'][-1].content)
    
if __name__ == "__main__":
    run()