"""
Facebook Post Reviewer Agent

This agent reviews Facebook posts for quality and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import ToolContext
from typing import Any, Dict

from .tools.gmail_utility import create_message, create_draft, authenticate_gmail
from ....constants import GEMINI_MODEL
import os
# Constants

def gmail_tool(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Call this function ONLY when the post meets all quality requirements and
    sending mail is required

    Args:
        tool_context: Context for tool execution

    Returns:
        Empty dictionary
    """
    try:
        service = authenticate_gmail()

        sender = os.getenv("GMAIL_SENDER")
        to = os.getenv("GMAIL_RECIPIENT")

        subject = "Meeting Minutes"
        message_text = tool_context.state.get("bengali_current_post")

        message = create_message(sender, to, subject, message_text)
        draft = create_draft(service, "me", message)

        return f"Email sent successfully! Draft id: {draft['id']}"
    except Exception as e:
        return f"Error sending email: {e}"
    return {}

# Define the Post Reviewer Agent
gmail_content = LlmAgent(
    name="GmailContent",
    model=GEMINI_MODEL,
    instruction="""You are an agent who calls the gmail_tool and mails the final response
    """,
    description="Mails the ",
    tools=[gmail_tool],
    output_key="bengali_review_feedback"
)
