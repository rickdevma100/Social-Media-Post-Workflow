"""
Facebook Post Refiner Agent

This agent refines Facebook posts based on review feedback.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search
from ....constants import GEMINI_MODEL



# Define the Post Refiner Agent
bengali_refiner = LlmAgent(
    name="BengaliRefinerAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Facebook Post Refiner.

    Your task is to refine a Facebook post based on review feedback.
    
    ## INPUTS
    **Current Post:**
    {bengali_current_post}
    
    **Review Feedback:**
    {bengali_review_feedback}
    
    ## TASK
    Carefully apply the feedback to improve the post.
    
    
    ## STYLE REQUIREMENTS
        1. Between 1000-1500 characters
        2. Include emojis
        3. Include Treanding hashtags
    
    ## OUTPUT INSTRUCTIONS
    - Output ONLY the refined post content
    - Do not add explanations or justifications
    """,
    description="Refines Facebook posts based on feedback to improve quality",
    output_key="bengali_current_post"
)