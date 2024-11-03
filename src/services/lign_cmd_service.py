from src.models.lign_cmd import LignCmd, LignCmdDAO

class LignCmdService:
    def __init__(self):
        self.dao = LignCmdDAO()

    def create_lign_cmd(self, qte, id_commande, id_produit):
        lign_cmd = LignCmd(qte=qte, id_commande=id_commande, id_produit=id_produit)
        return self.dao.create_lign_cmd(lign_cmd)

    def get_lign_cmd(self, lign_cmd_id):
        return self.dao.get_lign_cmd(lign_cmd_id)

    def update_lign_cmd(self, lign_cmd_id, new_data):
        return self.dao.update_lign_cmd(lign_cmd_id, new_data)

    def delete_lign_cmd(self, lign_cmd_id):
        return self.dao.delete_lign_cmd(lign_cmd_id)
