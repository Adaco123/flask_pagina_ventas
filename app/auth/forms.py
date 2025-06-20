from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(FlaskForm):
    nombre=StringField("NOMBRE", validators=[DataRequired(message="Este campo es obligatorio."), Length(max=64)])
    password=PasswordField("CONTRASEÑA", validators=[DataRequired(message="Este campo es obligatorio.")])
    email=StringField("EMAIL", validators=[DataRequired()])
    enviar=SubmitField("REGISTRAR")


class LoginForm(FlaskForm):
    email=StringField("EMAIL", validators=[DataRequired(message="Este campo es obligatorio.")])
    password=PasswordField("CONTRASEÑA", validators=[DataRequired(message="Este campo es obligatorio.")])
    remember_me=BooleanField("Recuerdame")
    enviar=SubmitField("ENTRAR")