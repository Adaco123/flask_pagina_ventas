from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm():
    titulo=StringField('Titulo', validators=[DataRequired(), Length(max=128)])
    content=TextAreaField('Contenido')
    enviar= SubmitField('Enviar')
