from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base, SessionLocal
from .commande import Commande

class Client(Base):
    __tablename__ = 'client'

    id_client = Column(Integer, primary_key=True, index=True)
    numero = Column(String(10))
    id_user = Column(Integer, ForeignKey('user.id_user'))

    commandes = relationship("Commande", back_populates="client")

class ClientDAO:
    def __init__(self):
        self.db = SessionLocal() 

    def create_client(self, client):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def get_client(self, client_id):
        return self.db.query(Client).filter(Client.id_client == client_id).first()

    def update_client(self, client_id, new_data):
        client = self.db.query(Client).filter(Client.id_client == client_id)
        if client:
            for key, value in new_data.items():
                setattr(client, key, value)
            self.db.commit
        return client
    
    def delete_client(self, client_id):
        client = self.db.query(Client).filter(Client.id_client == client_id)
        if client:
            self.db.delete(client)
            self.db.commit()

    def get_commandes_by_client_id(self, client_id):
        return self.db.query(Commande).filter(Commande.id_client == client_id).all()

        
