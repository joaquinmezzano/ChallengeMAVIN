from flask import Flask, request, jsonify
from agent import agent

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        response = agent.run(query)        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)