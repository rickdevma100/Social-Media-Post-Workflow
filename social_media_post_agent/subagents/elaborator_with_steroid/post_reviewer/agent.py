"""
Facebook Post Reviewer Agent

This agent reviews Facebook posts for quality and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from ...news_search_agent import news_search
from .tools import count_characters, exit_loop
from ....constants import GEMINI_MODEL
# Constants


# Define the Post Reviewer Agent
post_reviewer = LlmAgent(
    name="PostReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a Facebook Post Quality Reviewer.

    Your task is to evaluate the quality of a Facebook post about Agent Development Kit (ADK).
    
    ## EVALUATION PROCESS
    1. Use the count_characters tool to check the post's length.
       Pass the post text directly to the tool.
    
    2. If the length check fails (tool result is "fail"), provide specific feedback on what needs to be fixed.
       Use the tool's message as a guideline, but add your own professional critique.
    
    3. If length check passes, evaluate the post against these criteria:
       - REQUIRED ELEMENTS:
        1. Elaboration of the topic with personal touch and emotion. 
        2. Include keywords which have virality and which make people read the content.
        3. Make sure The content is written in simple and deep words.
       
       - STYLE REQUIREMENTS:
        1. Between 1000-1500 characters
        2. Include emojis
        3. Include Treanding hashtags
        4. Show genuine enthusiasm
        5. Remove [news_search] if any
    4. *Mandetorily Do call agent tool and after google search check the {searched_result} and provide specific feedback on what needs to be fixed.
       Do use agent tool until fact check passes.
    
    ## OUTPUT INSTRUCTIONS
    IF the post fails ANY of the checks above:
      - Return concise, specific feedback on what to improve
      
    ELSE IF the post meets ALL requirements:
      - Call the exit_loop function
      - Return "Post meets all requirements. Exiting the refinement loop."
      
    Do not embellish your response. Either provide feedback on what to improve OR call exit_loop and return the completion message.
    
    ## POST TO REVIEW
    {current_post}
    """,
    description="Reviews post quality and provides feedback on what to improve or exits the loop if requirements are met",
    tools=[AgentTool(news_search),count_characters, exit_loop],
    output_key="review_feedback",
)
