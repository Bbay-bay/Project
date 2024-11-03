# src/routes/produit_routes.py

from flask import Blueprint, request, jsonify
from src.services.produit_service import ProduitService

produit_bp = Blueprint('produits', __name__)
produit_service = ProduitService()

@produit_bp.route('/produits', methods=['POST'])
def add_produit():
    data = request.json
    libelle = data.get('libelle')
    prix = data.get('prix')

    if not libelle or prix is None:
        return jsonify({'error': 'Missing fields'}), 400

    new_produit = produit_service.create_produit(libelle, prix)
    return jsonify({
        'id_produit': new_produit.id_produit,
        'libelle': new_produit.libelle,
        'prix': new_produit.prix
    }), 201

@produit_bp.route('/produits/<int:produit_id>', methods=['GET'])
def get_produit(produit_id):
    produit = produit_service.get_produit(produit_id)
    if produit:
        return jsonify({
            'id_produit': produit.id_produit,
            'libelle': produit.libelle,
            'prix': produit.prix
        }), 200
    return jsonify({'error': 'Produit not found'}), 404

@produit_bp.route('/produits/<int:produit_id>', methods=['PUT'])
def update_produit(produit_id):
    data = request.json
    updated_produit = produit_service.update_produit(produit_id, data)
    if updated_produit:
        return jsonify({
            'id_produit': updated_produit.id_produit,
            'libelle': updated_produit.libelle,
            'prix': updated_produit.prix
        }), 200
    return jsonify({'error': 'Produit not found'}), 404

@produit_bp.route('/produits/<int:produit_id>', methods=['DELETE'])
def delete_produit(produit_id):
    produit_service.delete_produit(produit_id)
    return jsonify({'message': 'Produit deleted'}), 204
