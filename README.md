# ChallengeMAVIN

## Pre-requisitos
Linux/Ubuntu
Python3

## Pasos de instalación
### Entorno y librerias de Python
python -m venv venv
source venv/bin/activate
pip install -U langchain-community langgraph langchain-anthropic tavily-python langgraph-checkpoint-sqlite
pip install langchain langchain-ollama langchain-chroma

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
·Ollama: https://github.com/ollama/ollama/blob/main/docs/README.md
·Ollama & LangChain integration: https://python.langchain.com/docs/integrations/llms/ollama/
·Gemma2: https://ollama.com/library/gemma2:2b

# Problemas encontrados
·La mayoria de la documentación/tutoriales para utilizar LangChain lo hacen usando una API Key, no local con Ollama

# Cosas a explicar
·Elección del modelo de Ollama (Gemma2:2b)