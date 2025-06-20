from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed , FileField
class PostForm(FlaskForm):
    title=StringField('Titulo', validators=[DataRequired(message="Este campo es obligatorio."), Length(max=128)])
    content=TextAreaField('Contenido')
    post_image=FileField('Imagen de cabecera', validators=[FileAllowed(['jpg','png'], 'solo se permiten imagenes')])
    submit= SubmitField('Enviar')
class UserAdminForm(FlaskForm):
    es_admi = BooleanField('Administrador')
    submit = SubmitField('Guardar')