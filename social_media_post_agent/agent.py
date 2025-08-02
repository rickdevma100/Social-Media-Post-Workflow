from google.adk.agents import SequentialAgent

from .subagents.create_image import create_image_agent
from .subagents.gmail_content import gmail_content
from .subagents.news_search_agent import news_search
from .subagents.extractor.agent import summarize_from_search_agent
from .subagents.elaborator_with_steroid.agent import elaborator_agent
from .subagents.convert_into_bengali.agent import language_translation_agent
from .subagents.prompt_generator_for_image import prompt_generator_for_image

root_agent = SequentialAgent(
    name="social_media_post_agent",
    sub_agents=[news_search, summarize_from_search_agent, elaborator_agent, language_translation_agent,gmail_content],

)
