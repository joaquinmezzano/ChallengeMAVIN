# ChallengeMAVIN
Descipción

## Herramientas utilizadas
Python3
LangChain -> Framework para desarrollar aplicaciones con LLMs (Crear agentes, chatbots, entre otros)
Ollama -> Para correr nuestro modelo localmente
SerpAPI -> Herramienta de búsqueda en caso de necesitar información actual

## Pre-requisitos
Linux/Ubuntu
Python3

## Pasos de instalación
### Entorno y librerias de Python
python -m venv venv
source venv/bin/activate
pip install -U langchain-community langgraph langchain-anthropic tavily-python langgraph-checkpoint-sqlite
pip install langchain langchain-ollama langchain-chroma
pip install google-search-results //Para utilizar SerpAPI

### Ollama
sudo apt install curl
curl -fsSL https://ollama.com/install.sh | sh
Comprobamos instalación con el comando: ollama -v
Bajamos gemma2-2b: ollama pull gemma2:2b
    Podemos probarlo con: ollama run gemma2:2b

## Documentation
·LangChain: https://python.langchain.com/docs/introduction/
·Building an Agent: 
    -https://python.langchain.com/docs/tutorials/agents/
    -https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/06-langchain-agents.ipynb
    -https://www.youtube.com/watch?v=E4l91XKQSgw
·Agent types: https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html
·Ollama: https://github.com/ollama/ollama/blob/main/docs/README.md
·Ollama & LangChain integration: https://python.langchain.com/docs/integrations/llms/ollama/
·Ollama & Agents integration: https://python.langchain.com/api_reference/langchain/agents/langchain.agents.initialize.initialize_agent.html
·Gemma2: https://ollama.com/library/gemma2:2b
·SerpAPI: https://python.langchain.com/docs/integrations/tools/serpapi/

# Problemas encontrados -> Solución
·Evitar que las API key utilizadas (como la de SerpAPI) esten hardcodeadas -> Utilización de getpass para evitarlo.
·getpass es requerido cada vez que se ejecuta el programa -> 
·Definir que tipo de agente utilizar -> Elegi "ZERO_SHOT_REACT_DESCRIPTION" debido a que hace un razonamiento antes de dar una respuesta.