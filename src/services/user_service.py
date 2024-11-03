from ..models.user import User, UserDAO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, nom, login, password):
        new_user = User(nom=nom, login=login, password=password)
        return self.user_dao.create_user(new_user)

    def get_user(self, user_id):
        return self.user_dao.get_user(user_id)

    def update_user(self, user_id, new_data):
        return self.user_dao.update_user(user_id, new_data)

    def delete_user(self, user_id):
        self.user_dao.delete_user(user_id)
