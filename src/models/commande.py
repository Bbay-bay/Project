from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..config.database import Base, SessionLocal

class Commande(Base):
    __tablename__ = 'commande'

    id_commande = Column(Integer, primary_key=True, index=True)
    reference = Column(Integer)
    date = Column(Date)
    id_client = Column(Integer, ForeignKey('client.id_client'))

    client = relationship("Client", back_populates="commandes") 
    lign_cmds = relationship('LignCmd', back_populates='commande')

class CommandeDAO:
    def __init__(self):
        self.db = SessionLocal()

    def create_commande(self, commande):
        self.db.add(commande)
        self.db.commit()
        self.db.refresh(commande)
        return commande

    def get_commande(self, commande_id):
        return self.db.query(Commande).filter(Commande.id_commande == commande_id).first()

    def update_commande(self, commande_id, new_data):
        commande = self.db.query(Commande).filter(Commande.id_commande == commande_id).first()
        if commande:
            for key, value in new_data.items():
                setattr(commande, key, value)
            self.db.commit()
        return commande

    def delete_commande(self, commande_id):
        commande = self.db.query(Commande).filter(Commande.id_commande == commande_id).first()
        if commande:
            self.db.delete(commande)
            self.db.commit()
            
    def get_commandes_by_client_id(self, client_id):
        return self.db.query(Commande).filter(Commande.id_client == client_id).all()
