"""
Facebook Post Generator Agent

This agent generates the initial Facebook post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search
from ....constants import GEMINI_MODEL


# Define the Initial Post Generator Agent
initial_post_generator = LlmAgent(
    name="InitialBengaliPostGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a 30‑year veteran in Bengali literary expression.

    Please translate the following post `{current_post}` into Bengali, fully capturing its emotion and nuance—not just word‑for‑word. Write in simple yet profound language.  
    Your translation must be 1000–1500 characters long, include emojis for emotional emphasis, sprinkle in trending English hashtags (e.g., #Inspiration, #LifeGoals), and exude genuine enthusiasm.
    Choose at-most 7 english words keep those as it is, no need to translate it.
    ## STYLE REQUIREMENTS
    - Between 1000-2000 characters
    - Include emojis, But very less
    - Keep the place's name in English only
    - Take special care while you are translating the greetings.
    - Use Kolkata Bengali for sure do not Bangladeshi Bengali.
    - Please make sure all the verbs are wtitten in a proper way
    
    ## OUTPUT INSTRUCTIONS
    - Return only the translated post—no additional commentary, formatting tags, or explanations.
    """,
    description="Translate the Post into Bengali with Emotion",
    output_key="bengali_current_post"
)
