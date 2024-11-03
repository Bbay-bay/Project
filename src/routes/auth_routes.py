from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_jwt_extended import create_access_token, jwt_required
from flask_bcrypt import Bcrypt
from src.models.user import User, UserDAO  
from src.forms import RegistrationForm, LoginForm

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()
user_dao = UserDAO()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(nom=form.nom.data, login=form.login.data, password=hashed_password)
        user_dao.create_user(new_user)
        flash('Votre compte a été créé avec succès !', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = user_dao.get_user_by_login(form.login.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            access_token = create_access_token(identity={'id_user': user.id_user})
            flash('Vous êtes connecté avec succès !', 'success')
            return redirect(url_for('auth.protected'))  # Changez cela en redirigeant vers votre route protégée
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="This is a protected route."), 200
