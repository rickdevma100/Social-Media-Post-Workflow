"""
Facebook Post Generator Root Agent

This module defines the root agent for the Facebook post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .post_generator.agent import initial_post_generator
from .post_refiner.agent import post_refiner
from .post_reviewer.agent import post_reviewer

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="PostRefinementLoop",
    max_iterations=5,
    sub_agents=[
        post_reviewer,
        post_refiner,
    ],
    description="Iteratively reviews and refines a Facebook post until quality requirements are met",
)

# Create the Sequential Pipeline
elaborator_agent = SequentialAgent(
    name="ElaboratedPostGenerationPipeline",
    sub_agents=[
        initial_post_generator,  # Step 1: Generate initial post
        refinement_loop,  # Step 2: Review and refine in a loop

    ],
    description="Generates and refines a Facebook post through an iterative review process",
)
