from flask import Flask, request, jsonify
from langchain_ollama.llms import OllamaLLM
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool, initialize_agent #Contruir y usar el agente
from langchain.agents.agent_types import AgentType #Elegir el tipo de agente
import getpass
import os

app = Flask(__name__) # Instancia de Flask, inicializa el backend

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

# Mediante Flask preguntamos al agente y nos devuelve un JSON con la respuesta
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get("query", "") # Espera un valor query en el json extraido en data, usando "" como default
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        result = agent.run(query) # Intenta ejecutar el agente con el query recibido
        return jsonify({"response": result}) # Retorna la respuesta del agente en formato json
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)