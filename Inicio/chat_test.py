import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    promp = data.get('prompt', '')
    modelo = 'llama3.2'

    # Generar la respuesta usando el modelo local LLaMA a través de ollama
    response = ollama.chat(model=modelo, messages=[{'role': 'user', 'content': promp}])

    return jsonify({'response': response['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
