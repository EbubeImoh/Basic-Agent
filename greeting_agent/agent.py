# Make sure the correct package is installed; if not, install or update the import path.
# For example, if using the openai package:
# from openai import Agent

from google.adk.agents import Agent  # type: ignore # Update this line if the correct module is different

root_agent = Agent(
    name = "greeting_agent",
    model = "gemini-2.0-flash",
    description = "A simple agent that greets the user.",
    instruction = """
    You are a friendly agent that greets the user. 
    Ask for their name and greet them with their name.""",
)