"""
Facebook Post Generator Agent

This agent generates the initial Facebook post before refinement.
"""
from google.adk.agents.llm_agent import LlmAgent
from ...constants import GEMINI_MODEL


# Define the Initial Post Generator Agent
prompt_generator_for_image = LlmAgent(
    name="PromptGeneratorForImage",
    model=GEMINI_MODEL,
    instruction="""
    You are a 20 years experienced AI Artist and a prompt engineer.
    Your primary purpose is to generate ultra-detailed prompts collecting the keywords from the below text 
    which can be used to create a bright enough image.
    {current_post}
    """,
    description="Creates a prompt for generating image",
    output_key="image_prompt_generated"
)
