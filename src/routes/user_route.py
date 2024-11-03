from flask import Blueprint, request, jsonify
from ..services.user_service import UserService

user_service = UserService()
user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_service.create_user(data['nom'], data['login'], data['password'])
    return jsonify({"id_user": user.id_user, "nom": user.nom, "login": user.login}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({"id_user": user.id_user, "nom": user.nom, "login": user.login}), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = user_service.update_user(user_id, data)
    if user:
        return jsonify({"id_user": user.id_user, "nom": user.nom, "login": user.login}), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"}), 204
