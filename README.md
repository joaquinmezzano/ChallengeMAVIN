# Challenge MAVIN: Python
Your goal is to design and develop a backend application using Python for executing a LangChain agent that answers a question from the user using a web scraping tool. The system must have the following requirements:
- A **Python** backend that exposes and API endpoint where the user sends a query.
- This API endpoint triggers a **LangChain** agent implemented in Python, which:
	- Uses a **web search tool** via LangChain.
	- Utilizes a **local LLM via Ollama** using the official LangChain+Ollama integration.
	- Returns a response based on the user query.
- You MUST use the Ollama LangChain Python extension to run an LLM locally for your agent. (See the Ollama LangChain documentation.)

## 1. Tools
- Python3
- LangChain
- Ollama
    - Model: Mistral
- SerpAPI
- Flask

## 2. Prerequisites
- Ubuntu operative system.
- Python3.

## 3. Installation steps
##### 3.1 - Python Environment and Libraries
Create the Python virtual environment:
> `python -m venv venv`

Activate the virtual environment:
> `source venv/bin/activate`

Install the dependencies:
> `pip install -r requirements.txt`

##### 3.2 - Ollama
Install *curl*:
> `sudo apt install curl`

Download and install Ollama using *curl*:
> `curl -fsSL https://ollama.com/install.sh | sh`

Check that Ollama is correctly installed:
> `ollama -v`

Download the model to be used:
> `ollama pull mistral:7b`

## 4. Execution steps
In the first termanl, run the Ollama server:
> `ollama serve`

In a second terminal, activate the Python environment and run the *app.py* file:
> `source venv/bin/activate`
>> `python3 app.py`

In a third terminal, use *curl* to make a POST request with your question (replace the query with your own):
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
- ChatGPT y Google: used for generating trivial elements (keywords), research (suotable libraries/frameworks) and troubleshooting technical issues (library incompatibilities, installation errors)

## 6. Problemas encontrados
> **ISSUE:** Avoid hardcoding API keys (SerpAPI)  
> **SOLUTION:** Used *getpass* to prompt for input securely.

> **ISSUE:** *getpass* is required every time the program is executed.  
> **SOLUTION:** After considering other options (which involve hardcoding), i decided this is the most secure and flexible approach so i will not change it.

> **ISSUE:** Choosing the type of agent to use.  
> **SOLUTION:** I selected "ZERO_SHOT_REACT_DESCRIPTION" because it reasons step-by-step before giving a final answer.

> **ISSUE:** The agent always use SerpAPI to answers, instead of consulting Ollama locally. (This is a common issue with this kind of exercises)  
> **FIRST POSSIBLE SOLUTION:** Add a prompt at initialization to instruct the agent to only use Web Search when necesary. However, the selected agent type ignored this prompt.  
> **SECOND POSSIBLE SOLUTION:** Use another agent type such as "OPENAI_FUNCTIONS", but it requires paid models and does not support any Ollama model.  
> **THIRD POSSIBLE SOLUTION:** Implement a helper function to detect whether the question is related to current events (user SerpAPI) or not (use Ollama). This can be done using keywords, but it has many problems (keyword skip, brute force approach) **This is the solution i initially chose.**  
>> **FINAL SOLUTION:** The actual issue was my fault. I only added one tool (for web scrapping) to the agent, that caused the agent to only use that one. By adding a second tool (for using Ollama), the agent became capable of deciding which one to use based on the query.