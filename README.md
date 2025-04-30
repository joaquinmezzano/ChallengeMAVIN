# Challenge MAVIN: Python
Your goal is to design and develop a backend application using Python for executing a LangChain agent that answers a question from the user using a web scraping tool. The system must have the following requirements:
- A **Python** backend that exposes and API endpoint where the user sends a query.
- This API endpoint triggers a **LangChain** agent implemented in Python, which:
	- Uses a **web search tool** via LangChain.
	- Utilizes a **local LLM via Ollama** using the official LangChain+Ollama integration.
	- Returns a response based on the user query.
- You MUST use the Ollama LangChain Python extension to run an LLM locally for your agent. (See the Ollama LangChain documentation.)

## 1. Herramientas utilizadas
- Python3
- LangChain *(Framework para desarrollar aplicaciones con LLMs como crear agentes, chatbots, entre otros)*
- Ollama *(Para correr nuestro modelo localmente)*
- SerpAPI *(Herramienta de búsqueda en caso de necesitar información actual)*
- Flask *(Mini-framework que utilizo para construir APIs backend)*

## 2. Pre-requisitos
- Sistema operativo de tipo Linux/Ubuntu.
- Python3.

## 3. Pasos de instalación
##### 3.1 - Entorno y librerias de Python
> `python -m venv venv`
> `source venv/bin/activate`
> `pip install -U langchain-community langgraph langchain-anthropic tavily-python langgraph-checkpoint-sqlite`
> `pip install langchain langchain-ollama langchain-chroma`
> `pip install google-search-results`
> `pip install flask`

##### 3.2 - Ollama
> `sudo apt install curl`
> `curl -fsSL https://ollama.com/install.sh | sh`
> `ollama -v` --> para comprobar la instalación
> `ollama pull gemma2:2b`
> `ollama run gemma2:2b` --> para probar el modelo

## 4. Pasos de ejecución
##### 4.1 - Iniciar los servidores de Ollama y de Flask
> `ollama serve`
> `source venv/bin/activate`
> `python3 main.py`
 
##### 4.2 - Lanzar un curl (5000 puerto default) en otra terminar para probar funcionamiento:
> `curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"model": "gemma2:2b", "query": "What is the capital of Argentina?"}'`

## 5. Documentation
- LangChain: https://python.langchain.com/docs/introduction/
- Building an Agent: 
    - https://python.langchain.com/docs/tutorials/agents/
    - https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/06-langchain-agents.ipynb
    - https://www.youtube.com/watch?v=E4l91XKQSgw
- Agent types: https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html
- Ollama: https://github.com/ollama/ollama/blob/main/docs/README.md
- Ollama & LangChain integration: https://python.langchain.com/docs/integrations/llms/ollama/
- Ollama & Agents integration: https://python.langchain.com/api_reference/langchain/agents/langchain.agents.initialize.initialize_agent.html
- Gemma2: https://ollama.com/library/gemma2:2b
- SerpAPI: https://python.langchain.com/docs/integrations/tools/serpapi/
- Flask:
    - https://flask.palletsprojects.com/en/stable/
    - https://flask.palletsprojects.com/en/stable/quickstart/

## 6. Problemas encontrados
- Evitar que las API key utilizadas (como la de SerpAPI) esten hardcodeadas
    - **SOLUCIÓN**: Utilización de getpass para evitarlo.
- getpass es requerido cada vez que se ejecuta el programa.
    - **SOLUCIÓN**:
- Definir que tipo de agente utilizar.
    - **SOLUCIÓN**: Elegi "ZERO_SHOT_REACT_DESCRIPTION" debido a que hace un razonamiento antes de dar una respuesta.
- Creo que siempre busca la respuesta por SerpAPI en lugar de preguntar localmente a Ollama.
    - **SOLUCIÓN**: 