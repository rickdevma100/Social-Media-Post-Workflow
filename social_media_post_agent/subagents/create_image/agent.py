"""
Facebook Post Generator Agent

This agent generates the initial Facebook post before refinement.
"""
from google.adk.agents.llm_agent import LlmAgent

from .tools import create_image
from ...constants import GEMINI_MODEL


# Define the Initial Post Generator Agent
create_image_agent = LlmAgent(
    name="CreateImage",
    model=GEMINI_MODEL,
    instruction="""
    You are a Image Generator, responsible for taking refined prompts
    and generating actual images using OpenAI's image generation API.
    
    ## Your Role
    
    Your job is to:
    1. Receive a detailed image prompt from the prompt_generator_for_image agent
    2. The create_image tool will automatically use all available assets
    
    """,
    description="Creates an Image",
    tools = [create_image]
)
