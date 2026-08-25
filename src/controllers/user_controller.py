from flask import Blueprint, request, jsonify
from src.repository.user_repository import user_repository
from src.utils.validators import validate_user_payload

user_bp = Blueprint('users', __name__, url_prefix='/users')

# 1. LISTAR TODOS OS USUÁRIOS
@user_bp.route('', methods=['GET'])
def get_users():
    users = user_repository.list_all()
    return jsonify({
        "status": "success",
        "data": users
    }), 200


# 2. CADASTRAR NOVO USUÁRIO
@user_bp.route('', methods=['POST'])
def create_user():
    data = request.get_json(silent=True)

    # Validação
    is_valid, error_message = validate_user_payload(data, is_update=False)
    if not is_valid:
        return jsonify({
            "status": "fail",
            "error": {
                "code": "BAD_REQUEST",
                "details": error_message
            }
        }), 400

    # Verifica duplicidade de e-mail
    email_limpo = data["email"].strip().lower()
    users = user_repository.list_all()
    if any(user["email"].lower() == email_limpo for user in users):
        return jsonify({
            "status": "fail",
            "error": {
                "code": "DUPLICATE_EMAIL",
                "details": f"O e-mail '{email_limpo}' ja esta cadastrado no sistema."
            }
        }), 400

    # Criação e resposta
    payload_sanitizado = {
        "nome": data["nome"].strip(),
        "email": email_limpo
    }
    new_user = user_repository.create(payload_sanitizado)

    return jsonify({
        "status": "success",
        "message": "Usuario cadastrado com sucesso!",
        "data": new_user
    }), 201


# 3. BUSCAR USUÁRIO POR ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id: int):
    user = user_repository.find_by_id(user_id)

    if not user:
        return jsonify({
            "status": "fail",
            "error": {
                "code": "NOT_FOUND",
                "details": f"Usuario com ID {user_id} nao foi encontrado."
            }
        }), 404

    return jsonify({
        "status": "success",
        "data": user
    }), 200


# 4. ATUALIZAR USUÁRIO
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    data = request.get_json(silent=True)

    is_valid, error_message = validate_user_payload(data, is_update=True)
    if not is_valid:
        return jsonify({
            "status": "fail",
            "error": {
                "code": "BAD_REQUEST",
                "details": error_message
            }
        }), 400

    updated_user = user_repository.update(user_id, data)

    if not updated_user:
        return jsonify({
            "status": "fail",
            "error": {
                "code": "NOT_FOUND",
                "details": f"Nao foi possível atualizar. Usuario com ID {user_id} nao foi encontrado."
            }
        }), 404

    return jsonify({
        "status": "success",
        "message": "Usuario atualizado com sucesso!",
        "data": updated_user
    }), 200


# 5. REMOVER USUÁRIO
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    success = user_repository.delete(user_id)

    if not success:
        return jsonify({
            "status": "fail",
            "error": {
                "code": "NOT_FOUND",
                "details": f"Nao foi possível remover. Usuario com ID {user_id} nao foi encontrado."
            }
        }), 404

    return jsonify({
        "status": "success",
        "message": f"Usuario com ID {user_id} removido com sucesso."
    }), 200