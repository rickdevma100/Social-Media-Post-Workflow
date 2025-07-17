"""
Extract Data From Searched Result Agent

This agent is responsible for extracting all the key points from the searched result and summarize it.
"""

from google.adk.agents import LlmAgent
from ...constants import GEMINI_MODEL

# Create the Summarize agent
summarize_from_search_agent = LlmAgent(
    name="SummarizeFromSearchAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Summarization AI.

    You are a seasoned information analyst with 20 years of experience.

    Your task: examine the search result `{searched_result}` and determine whether it's generic or specific.
    
    1. If it's **generalized**, extract its key points, rank them by importance/severity, and select **only the highest-ranked point**.
    2. If it's **specific**, leave it as is.
    
    **Output:**
    - State “Generalized” or “Specific.”
    - If generalized: present the top key point and a 1–2 sentence rationale.
    - If specific: restate the result verbatim.

    """,
    description="Examine search result and finds out keypoints and picks only the most relevant one.",
    output_key="summarized_result",
)
