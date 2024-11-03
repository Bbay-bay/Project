from src.models.produit import Produit, ProduitDAO

class ProduitService:
    def __init__(self):
        self.dao = ProduitDAO()

    def create_produit(self, libelle, prix):
        produit = Produit(libelle=libelle, prix=prix)
        return self.dao.create_produit(produit)

    def get_produit(self, produit_id):
        return self.dao.get_produit(produit_id)

    def update_produit(self, produit_id, new_data):
        return self.dao.update_produit(produit_id, new_data)

    def delete_produit(self, produit_id):
        return self.dao.delete_produit(produit_id)
