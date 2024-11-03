from ..models.client import Client, ClientDAO

class ClientService:
    def __init__(self):
        self.client_dao = ClientDAO()
        
    def create_client(self, numero, id_user):
        client = Client(numero = numero, id_user = id_user)  
        return self.client_dao.create_client(client) 
    
    def get_client(self, clinet_id):
        return self.client_dao.get_client(clinet_id)
    
    def update_client(self, client_id, new_data):
        return self.client_dao.update_client(client_id, new_data)
    
    def delete_client(self, client_id):
        self.client_dao.delete_client(client_id)