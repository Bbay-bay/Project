from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base, SessionLocal

class LignCmd(Base):
    __tablename__ = 'lign_cmd'

    id_lign_cmd = Column(Integer, primary_key=True, index=True)
    qte = Column(Float)
    id_commande = Column(Integer, ForeignKey('commande.id_commande'))
    id_produit = Column(Integer, ForeignKey('produit.id_produit'))

    commande = relationship("Commande", back_populates="lign_cmds")
    produit = relationship("Produit")

class LignCmdDAO:
    def __init__(self):
        self.db = SessionLocal()

    def create_lign_cmd(self, lign_cmd):
        self.db.add(lign_cmd)
        self.db.commit()
        self.db.refresh(lign_cmd)
        return lign_cmd

    def get_lign_cmd(self, lign_cmd_id):
        return self.db.query(LignCmd).filter(LignCmd.id_lign_cmd == lign_cmd_id).first()

    def update_lign_cmd(self, lign_cmd_id, new_data):
        lign_cmd = self.db.query(LignCmd).filter(LignCmd.id_lign_cmd == lign_cmd_id).first()
        if lign_cmd:
            for key, value in new_data.items():
                setattr(lign_cmd, key, value)
            self.db.commit()
        return lign_cmd

    def delete_lign_cmd(self, lign_cmd_id):
        lign_cmd = self.db.query(LignCmd).filter(LignCmd.id_lign_cmd == lign_cmd_id).first()
        if lign_cmd:
            self.db.delete(lign_cmd)
            self.db.commit()
