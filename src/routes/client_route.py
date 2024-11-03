from flask import Blueprint, request, jsonify
from ..services.client_service import ClientService

client_service = ClientService()
client_bp = Blueprint('client', __name__)

@client_bp.route('/clients', methods=['POST'])
def add_client():
    data = request.json
    numero = data.get('numero')
    id_user = data.get('id_user')
    
    if not numero or not id_user:
        return jsonify({'error': 'Missing fields'}), 400

    new_client = client_service.create_client(numero, id_user)
    return jsonify({
        'id_client': new_client.id_client,
        'numero': new_client.numero,
        'id_user': new_client.id_user
    }), 201

@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = client_service.get_client(client_id)
    if client:
        return jsonify({
            'id_client': client.id_client,
            'numero': client.numero,
            'id_user': client.id_user
        }), 200
    return jsonify({'error': 'Client not found'}), 404

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    updated_client = client_service.update_client(client_id, data)
    if updated_client:
        return jsonify({
            'id_client': updated_client.id_client,
            'numero': updated_client.numero,
            'id_user': updated_client.id_user
        }), 200
    return jsonify({'error': 'Client not found'}), 404

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client_service.delete_client(client_id)
    return jsonify({'message': 'Client deleted'}), 204