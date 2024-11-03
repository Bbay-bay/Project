from sqlalchemy import Column, Integer, String, Float
from ..config.database import Base, SessionLocal

class Produit(Base):
    __tablename__ = 'produit'

    id_produit = Column(Integer, primary_key=True, index=True)
    libelle = Column(String(255))
    prix = Column(Float)

class ProduitDAO:
    def __init__(self):
        self.db = SessionLocal()

    def create_produit(self, produit):
        self.db.add(produit)
        self.db.commit()
        self.db.refresh(produit)
        return produit

    def get_produit(self, produit_id):
        return self.db.query(Produit).filter(Produit.id_produit == produit_id).first()

    def update_produit(self, produit_id, new_data):
        produit = self.db.query(Produit).filter(Produit.id_produit == produit_id).first()
        if produit:
            for key, value in new_data.items():
                setattr(produit, key, value)
            self.db.commit()
        return produit

    def delete_produit(self, produit_id):
        produit = self.db.query(Produit).filter(Produit.id_produit == produit_id).first()
        if produit:
            self.db.delete(produit)
            self.db.commit()
