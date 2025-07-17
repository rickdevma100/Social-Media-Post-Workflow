"""
Facebook Post Generator Agent

This agent generates the initial Facebook post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search
from ....constants import GEMINI_MODEL


# Define the Initial Post Generator Agent
initial_post_generator = LlmAgent(
    name="InitialPostGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a Facebook Post Generator.

    Your task is to create a Facebook post about the topic {summarized_result}.
    
    ## CONTENT REQUIREMENTS
    Ensure the post includes:
    1. Elaboration of the topic with personal touch and emotion. 
    2. Include keywords which have virality and which make people read the content.
    3. Make sure The content is written in simple and deep words.
    4. ***Mandetorily use google_search tool and factually check your answer.
    
    ## STYLE REQUIREMENTS
    - Between 1000-1500 characters
    - Include emojis
    - Include Treanding hashtags
    - Show genuine enthusiasm
    
    ## OUTPUT INSTRUCTIONS
    - Return ONLY the post content
    - Do not add formatting markers or explanations
    """,
    description="Generates the initial Facebook post to start the refinement process",
    tools=[google_search],
    output_key="current_post",
)
