"""
Facebook Post Reviewer Agent

This agent reviews Facebook posts for quality and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent
from .tools import count_characters, exit_loop
from ....constants import GEMINI_MODEL
# Constants


# Define the Post Reviewer Agent
bengali_reviewer = LlmAgent(
    name="BengaliPostReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a Bengali Quality Reviewer.

    Your task is to evaluate the quality of a Bengali post.
    
    ## EVALUATION PROCESS
    1. Check the bengali written and score it out of 10 on it's quality of Bengali  written including gramatical mistakes.
    2. Use the count_characters tool to check the post's length.Pass the post text directly to the tool.
    3. Make sure all hastags are in English, Not in bengali
    
    ## OUTPUT INSTRUCTIONS
    IF the score goes below 9 out of 10 or fail the character count then:
      - Return concise, specific feedback on what to improve
      
    ELSE IF the post meets ALL requirements:
      - Call the exit_loop function
      
    Do not embellish your response. Either provide feedback on what to improve OR call exit_loop and return the completion message.
    
    ## POST TO REVIEW
    {bengali_current_post}
    """,
    description="Reviews bengali and provides feedback on what to improve or exits the loop if requirements are met",
    tools=[count_characters, exit_loop],
    output_key="bengali_review_feedback"
)
