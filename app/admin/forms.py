from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title=StringField('Titulo', validators=[DataRequired(), Length(max=128)])
    content=TextAreaField('Contenido')
    submit= SubmitField('Enviar')
class UserAdminForm(FlaskForm):
    es_admi = BooleanField('Administrador')
    submit = SubmitField('Guardar')