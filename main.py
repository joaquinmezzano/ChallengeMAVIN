from langchain_ollama.llms import OllamaLLM
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool, initialize_agent #Contruir y usar el agente
from langchain.agents.agent_types import AgentType #Elegir el tipo de agente
import getpass
import os

# Obtenemos API key de SerpAPI
if not os.environ.get("SERPAPI_API_KEY"):
    os.environ["SERPAPI_API_KEY"] = getpass.getpass("Enter API key for SERPAPI: ")

# Configuramos herramienta de búsqueda para el agente
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run, #Utiliza la función search de SerpAPI
        description="Useful for answering questions about current events or factual data from the web." #Prompt interno del agente para decidir si usar esta herramienta o no.
    )
]

# Modelo Ollama
model = OllamaLLM(model="gemma2:2b")

# Agente con Ollama + SerpAPI
agent = initialize_agent(
    tools=tools,
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True #Imprime el razonamiento del agente, sirve para debugear
)

# Loop interactivo
while True:
    question = input("Ask the Agent (q to quit): ")
    if question == "q": break
    try:
        result = agent.run(question)
        print(result)
    except Exception as e:
        print("Error: ", e)