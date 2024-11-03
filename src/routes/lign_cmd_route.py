from flask import Blueprint, request, jsonify
from src.services.lign_cmd_service import LignCmdService

lign_cmd_bp = Blueprint('lign_cmds', __name__)
lign_cmd_service = LignCmdService()

@lign_cmd_bp.route('/lign_cmds', methods=['POST'])
def add_lign_cmd():
    data = request.json
    qte = data.get('qte')
    id_commande = data.get('id_commande')
    id_produit = data.get('id_produit')

    if qte is None or id_commande is None or id_produit is None:
        return jsonify({'error': 'Missing fields'}), 400

    new_lign_cmd = lign_cmd_service.create_lign_cmd(qte, id_commande, id_produit)
    return jsonify({
        'id_lign_cmd': new_lign_cmd.id_lign_cmd,
        'qte': new_lign_cmd.qte,
        'id_commande': new_lign_cmd.id_commande,
        'id_produit': new_lign_cmd.id_produit
    }), 201

@lign_cmd_bp.route('/lign_cmds/<int:lign_cmd_id>', methods=['GET'])
def get_lign_cmd(lign_cmd_id):
    lign_cmd = lign_cmd_service.get_lign_cmd(lign_cmd_id)
    if lign_cmd:
        return jsonify({
            'id_lign_cmd': lign_cmd.id_lign_cmd,
            'qte': lign_cmd.qte,
            'id_commande': lign_cmd.id_commande,
            'id_produit': lign_cmd.id_produit
        }), 200
    return jsonify({'error': 'Lign_cmd not found'}), 404

@lign_cmd_bp.route('/lign_cmds/<int:lign_cmd_id>', methods=['PUT'])
def update_lign_cmd(lign_cmd_id):
    data = request.json
    updated_lign_cmd = lign_cmd_service.update_lign_cmd(lign_cmd_id, data)
    if updated_lign_cmd:
        return jsonify({
            'id_lign_cmd': updated_lign_cmd.id_lign_cmd,
            'qte': updated_lign_cmd.qte,
            'id_commande': updated_lign_cmd.id_commande,
            'id_produit': updated_lign_cmd.id_produit
        }), 200
    return jsonify({'error': 'Lign_cmd not found'}), 404

@lign_cmd_bp.route('/lign_cmds/<int:lign_cmd_id>', methods=['DELETE'])
def delete_lign_cmd(lign_cmd_id):
    lign_cmd_service.delete_lign_cmd(lign_cmd_id)
    return jsonify({'message': 'Lign_cmd deleted'}), 204
