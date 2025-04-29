from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="gemma2:2b")

template = """
    You are an educated teacher and chef with focus on Argentinian gastronomy.

    Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    question = input("Ask the Argentinian chef (q to quit): ")
    if question == "q": break
    else:
        result = chain.invoke({"question": question})
        print(result)