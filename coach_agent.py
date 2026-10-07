import os
from anthropic import Anthropic
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, get_drill_prompt, get_session_prompt

# Load environment variables
load_dotenv()

# Initialize the Anthropic client
client = Anthropic()
model = "claude-sonnet-4-5-20250929"


def chat(messages, system=None):
    """Send messages to Claude and return the response."""
    params = {
        "model": model,
        "max_tokens": 2000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    
    # Find the first TextBlock
    for block in message.content:
        if block.type == "text":
            return block.text
    return "No text response found"


def generate_drill(drill_description, language="English"):
    """Generate a U8 coaching drill from a description."""
    messages = []
    messages.append({
        "role": "user",
        "content": get_drill_prompt(drill_description, language)
    })
    
    return chat(messages, system=SYSTEM_PROMPT)


def generate_session(session_theme, duration_minutes=60, language="English"):
    """Generate a complete U8 session plan."""
    messages = []
    messages.append({
        "role": "user",
        "content": get_session_prompt(session_theme, duration_minutes, language)
    })
    
    return chat(messages, system=SYSTEM_PROMPT)