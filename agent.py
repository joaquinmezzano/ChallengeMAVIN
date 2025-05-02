from langchain_ollama.llms import OllamaLLM
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
import getpass
import os

if not os.environ.get("SERPAPI_API_KEY"):
    os.environ["SERPAPI_API_KEY"] = getpass.getpass("Enter API key for SERPAPI: ")

model = OllamaLLM(model="mistral:7b")
search = SerpAPIWrapper()

tools = [
    Tool(
        name="Web search",
        func=search.run,
        description="Useful for answering questions about current events or factual data from the web."
    ),
    Tool(
        name="Local search",
        func=model,
        description="Useful for general knowledge, reasoning, and answering questions without needing real-time data."
    )
]

system_prompt = """
You are a helpful AI assistant. First, try to answer based on your own knowledge, using the "Local search" tool. Only use the "Web search" tool if the question is clearly about something that happened very recently or is not known to the general public.
These are your only Tools, do not attempt to use any others.
If possible aim to provide detailed and well-developed answers.
"""

agent = initialize_agent(
    tools=tools,
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={"system_message": system_prompt},
    handle_parsing_errors=True
)