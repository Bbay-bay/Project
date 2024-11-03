from sqlalchemy import Column, Integer, String
from ..config.database import Base, SessionLocal

class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    login = Column(String(255), unique=True)
    password = Column(String(255))

class UserDAO:
    def __init__(self):
        self.db = SessionLocal()

    def create_user(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id):
        return self.db.query(User).filter(User.id_user == user_id).first()

    def update_user(self, user_id, new_data):
        user = self.db.query(User).filter(User.id_user == user_id).first()
        if user:
            for key, value in new_data.items():
                setattr(user, key, value)
            self.db.commit()
        return user

    def delete_user(self, user_id):
        user = self.db.query(User).filter(User.id_user == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            
    def get_user_by_login(self, login):
        return self.db.query(User).filter(User.login == login).first()
