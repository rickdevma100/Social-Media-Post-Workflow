"""
Facebook Post Generator Agent

This agent generates the initial Facebook post before refinement.
"""
from google.adk.agents import LoopAgent, SequentialAgent
from google.adk.agents.llm_agent import LlmAgent
from .post_generator.agent import initial_post_generator
from .bengali_reviewer.agent import bengali_reviewer
from .bengali_refiner.agent import bengali_refiner

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="PostRefinementLoop",
    max_iterations=1,
    sub_agents=[
        bengali_reviewer,
        bengali_refiner,
    ],
    description="Iteratively reviews and refines a Facebook post until quality requirements are met",
)

# Define the Initial Post Generator Agent
language_translation_agent = SequentialAgent(
    name="BengaliGenerationPipeline",
    sub_agents=[
        initial_post_generator,  # Step 1: Generate initial post
        refinement_loop,  # Step 2: Review and refine in a loop

    ],
    description="Generates and refines a Facebook post through an iterative review process",
)