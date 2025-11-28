import os
import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """This tool gets the city and reutrns the Tempreature detail"""
    api_key = os.getenv("WHEATHER_API_KEY")
    if not api_key:
        return f"Could not fetch real weather for {city}, but it's probably sunny 😉"
    url = f"https://api.weatherstack.com/current?access_key={api_key}&query={city}"
    resp = requests.get(url)
    data = resp.json()
    return f"Weather in {city}: {data['current']['temperature']}°C, {data['current']['weather_descriptions'][0]}"

search_tool = DuckDuckGoSearchRun()

agent = create_agent(
    model="openai:gpt-4o",
    tools=[get_weather, search_tool],
    system_prompt="You are a helpful assistant that can answer factual questions using web search and fetch weather when asked."
)

def run_agent(user_input: str):
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })
    for m in result["messages"]:
        role = m.__class__.__name__
        content = getattr(m, "text", getattr(m, "content", ""))
        print(f"{role}: {content}")

if __name__ == "__main__":
    run_agent("What’s the capital of France and what’s the current weather there?")
