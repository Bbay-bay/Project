from .routes.user_route import user_bp
from .routes.client_route import client_bp
from .routes.commande_route import commande_bp
from .routes.produit_route import produit_bp
from .routes.lign_cmd_route import lign_cmd_bp
from .routes.auth_routes import auth_bp
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask import flash



app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'  # Changez ceci pour une vraie clé secrète
app.config['JWT_SECRET_KEY'] = 'votre_jwt_secret_key'  # Changez ceci pour une vraie clé secrète pour JWT
csrf = CSRFProtect(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)


# Register the user routes
app.register_blueprint(user_bp)
app.register_blueprint(client_bp)
app.register_blueprint(commande_bp)
app.register_blueprint(produit_bp)
app.register_blueprint(lign_cmd_bp)
app.register_blueprint(auth_bp)
app.secret_key = 'your_secret_key'  # Changez ceci pour une vraie clé secrète


@app.route('/')
def home():
    return "Welcome to the User API!"


if __name__ == '__main__':
    app.run(debug=True)
