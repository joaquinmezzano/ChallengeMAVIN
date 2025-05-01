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

agent = initialize_agent(
    tools=tools,
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)