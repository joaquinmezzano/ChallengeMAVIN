from flask import Flask, request, jsonify
from agent import agent, model

app = Flask(__name__) # Instancia de Flask, inicializa el backend

# Mediante Flask preguntamos al agente y nos devuelve un JSON con la respuesta
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get("query", "") # Espera un valor query en el json extraido en data, usando "" como default
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        response = agent.run(query)        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)