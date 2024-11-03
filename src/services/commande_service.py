from src.models.commande import Commande, CommandeDAO

class CommandeService:
    def __init__(self):
        self.dao = CommandeDAO()

    def create_commande(self, reference, date, id_client):
        commande = Commande(reference=reference, date=date, id_client=id_client)
        return self.dao.create_commande(commande)

    def get_commande(self, commande_id):
        return self.dao.get_commande(commande_id)

    def update_commande(self, commande_id, new_data):
        return self.dao.update_commande(commande_id, new_data)

    def delete_commande(self, commande_id):
        return self.dao.delete_commande(commande_id)
    
    def get_commandes_by_client_id(self, client_id):
        return self.dao.get_commandes_by_client_id(client_id)
