import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Importa o Blueprint contendo as rotas da API
from src.controllers.user_controller import user_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

# Registra as rotas de usuários na aplicação
app.register_blueprint(user_bp)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "online",
        "message": "API de Gerenciamento de Usuarios operando com sucesso!",
        "version": "1.0.0"
    }), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

    app.run(host='0.0.0.0', port=port, debug=debug_mode)