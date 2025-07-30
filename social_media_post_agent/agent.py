from google.adk.agents import SequentialAgent
from .subagents.news_search_agent import news_search
from .subagents.extractor.agent import summarize_from_search_agent
from .subagents.elaborator_with_steroid.agent import elaborator_agent
from .subagents.convert_into_bengali.agent import language_translation_agent
from .subagents.convert_into_bengali.gmail_content import gmail_content


root_agent = SequentialAgent(
    name="social_media_post_agent",
    sub_agents=[news_search, summarize_from_search_agent, elaborator_agent, language_translation_agent,gmail_content],
)
