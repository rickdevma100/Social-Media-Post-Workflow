from google.adk.agents import Agent
from google.adk.tools import google_search
from ..constants import GEMINI_MODEL

news_search = Agent(
    name="news_search",
    model="gemini-2.0-flash",
    description="News analyst agent",
    instruction="""
   You are a helpful assistant that can use the following tools:
        - google_search
    """,
    tools=[google_search],
    output_key="searched_result"

)
