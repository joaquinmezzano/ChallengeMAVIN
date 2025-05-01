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
- LangChain
- Ollama
    - Modelo: Mistral
- SerpAPI
- Flask

## 2. Pre-requisitos
- Sistema operativo Ubuntu.
- Python3.

## 3. Pasos de instalación
##### 3.1 - Entorno y librerias de Python
Creamos el entorno de Python:
> `python -m venv venv`

Entramos en el entorno de Python:
> `source venv/bin/activate`

Instalamos las dependencias:
> `pip install -r requirements.txt`

##### 3.2 - Ollama
Instalamos curl:
> `sudo apt install curl`

Bajamos el paquete de Ollama y lo instalamos con curl:
> `curl -fsSL https://ollama.com/install.sh | sh`

Comprobamos que Ollama este instalado correctamente:
> `ollama -v`

Bajamos el modelo que vamos a utilizar:
> `ollama pull mistral:7b`

## 4. Pasos de ejecución
En una primer consola ejecutamos el servidor de Ollama:
> `ollama serve`

En una segunda consola entramos en el entorno de Python y ejecutamos el archivo main.py:
> `source venv/bin/activate`
>> `python3 app.py`

En una tercer consola usamos curl para tirar un POST con la pregunta que queremos (cambiando el query por nuestra pregunta):
> `curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"query": "What is the capital of Argentina?"}'`

## 5. Documentation & Resources
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
- SerpAPI: 
    - https://python.langchain.com/docs/integrations/tools/serpapi/
    - https://serpapi.com/dashboard
- Flask:
    - https://flask.palletsprojects.com/en/stable/
    - https://flask.palletsprojects.com/en/stable/quickstart/
- ChatGPT y Google: generación de elementos triviales (como las keyword), investigación (ver framworks/librerias que me servian) y resolución de problemas técnicos (mal funcionamiento entre librerias, errores de instalación, etc.)

## 6. Problemas encontrados
- Evitar que las API key utilizadas (como la de SerpAPI) esten hardcodeadas
    - **SOLUCIÓN:** Utilización de getpass para evitarlo.
- getpass es requerido cada vez que se ejecuta el programa.
    - **SOLUCIÓN:** 
- Definir que tipo de agente utilizar.
    - **SOLUCIÓN:** Elegi "ZERO_SHOT_REACT_DESCRIPTION" debido a que hace un razonamiento en cada paso antes de dar una respuesta final.
- Siempre busca la respuesta por SerpAPI en lugar de preguntar localmente a Ollama (Esto resulto ser un problema muy común al trabajar con este tipo de ejercicio)
    - **POSIBLE SOLUCIÓN 1:** Añadir un prompt para darle al agente apenas se inicie para que solo utilice Search cuando sea realmente necesario. El problema es que el tipo de agente que utilizamos directamente ignora esto y siempre llama a Search.
    - **POSIBLE SOLUCIÓN 2:** Utilizar otro tipo de agente como "OPENAI_FUNCTIONS" pero el problema es que este utiliza modelos que son de pago para funcionar ya que este agente no soporta modelos de Ollama.
    - **POSIBLE SOLUCIÓN 3:** Utilizar una función auxiliar para que detecte si estamos ante una pregunta sobre actualidad (respondemos utilizando SerpAPI) u otro tipo de pregunta (respondemos utilizando el modelo local de Ollama). Esto se resuelve utilizando keywords y comprobando si la pregunta tiene estas mismas. **ESTA FUE LA OPCIÓN QUE ELEGI.**

## 7. Posibles problemas a la implementación actual
- Que la pregunta sea sobre algo que necesita información actual pero que se saltee las keywords, haciendo que Ollama responda (con información desactualizada) en lugar de hacer web scrapping con SerpAPI.