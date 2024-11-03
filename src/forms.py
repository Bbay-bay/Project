from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField , StringField, PasswordField
from wtforms.validators import DataRequired, Length

class CommandeForm(FlaskForm):
    reference = IntegerField('Référence', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    id_client = IntegerField('ID Client', validators=[DataRequired()])
    submit = SubmitField('Ajouter Commande')

class RegistrationForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('S\'inscrire')

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')