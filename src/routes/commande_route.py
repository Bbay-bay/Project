from flask import Blueprint, request, jsonify
from src.services.commande_service import CommandeService

from flask import Blueprint, render_template, redirect, url_for, flash
from src.forms import CommandeForm
from src.models.commande import Commande

commande_bp = Blueprint('commandes', __name__)
commande_service = CommandeService()

@commande_bp.route('/commandes', methods=['POST'])
def add_commande():
    data = request.json
    reference = data.get('reference')
    date = data.get('date')
    id_client = data.get('id_client')
    
    if not reference or not date or not id_client:
        return jsonify({'error': 'Missing fields'}), 400

    new_commande = commande_service.create_commande(reference, date, id_client)
    return jsonify({
        'id_commande': new_commande.id_commande,
        'reference': new_commande.reference,
        'date': new_commande.date,
        'id_client': new_commande.id_client
    }), 201

@commande_bp.route('/commandes/<int:commande_id>', methods=['GET'])
def get_commande(commande_id):
    commande = commande_service.get_commande(commande_id)
    if commande:
        return jsonify({
            'id_commande': commande.id_commande,
            'reference': commande.reference,
            'date': commande.date,
            'id_client': commande.id_client
        }), 200
    return jsonify({'error': 'Commande not found'}), 404

@commande_bp.route('/commandes/<int:commande_id>', methods=['PUT'])
def update_commande(commande_id):
    data = request.json
    updated_commande = commande_service.update_commande(commande_id, data)
    if updated_commande:
        return jsonify({
            'id_commande': updated_commande.id_commande,
            'reference': updated_commande.reference,
            'date': updated_commande.date,
            'id_client': updated_commande.id_client
        }), 200
    return jsonify({'error': 'Commande not found'}), 404

@commande_bp.route('/commandes/<int:commande_id>', methods=['DELETE'])
def delete_commande(commande_id):
    commande_service.delete_commande(commande_id)
    return jsonify({'message': 'Commande deleted'}), 204

@commande_bp.route('/clients/<int:client_id>/commandes', methods=['GET'])
def get_commandes_by_client(client_id):
    commandes = commande_service.get_commandes_by_client_id(client_id)
    if not commandes:
        return jsonify({'message': 'Aucune commande trouvée pour ce client.'}), 404

    result = [
        {
            'id_commande': commande.id_commande,
            'reference': commande.reference,
            'date': commande.date.strftime('%Y-%m-%d')
        } for commande in commandes
    ]
    return jsonify(result), 200

@commande_bp.route('/ajouter_commande', methods=['GET', 'POST'])
def ajouter_commande():
    form = CommandeForm()
    if form.validate_on_submit():
        nouvelle_commande = Commande(
            reference=form.reference.data,
            date=form.date.data,
            id_client=form.id_client.data
        )
        commande_service.dao.create_commande(nouvelle_commande)  # Assurez-vous que cette méthode existe
        flash('Commande ajoutée avec succès!', 'success')
        return redirect(url_for('commandes.ajouter_commande'))  # Redirige vers la même page après ajout

    return render_template('ajouter_commande.html', form=form)