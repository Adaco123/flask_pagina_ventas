from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(FlaskForm):
    nombre=StringField("NOMBRE", validators=[DataRequired(), Length(max=64)])
    password=PasswordField("CONTRASEÑA", validators=[DataRequired()])
    email=StringField("EMAIL", validators=[DataRequired()])
    enviar=SubmitField("REGISTRAR")


class LoginForm(FlaskForm):
    email=StringField("EMAIL", validators=[DataRequired()])
    password=PasswordField("CONTRASEÑA", validators=[DataRequired()])
    remember_me=BooleanField("Recuerdame")
    enviar=SubmitField("ENTRAR")