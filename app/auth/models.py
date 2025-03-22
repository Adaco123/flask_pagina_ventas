from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model, UserMixin):
    __tablename__="usuarios"

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(256), unique=True, nullable=False)
    contra=db.Column(db.String(200), nullable=False)
    es_admi=db.Column(db.Boolean, default=False)
      
    def __init__(self, nombre, email):
        self.nombre=nombre
        self.email=email
    
    def __repr__(self):
        return f'<User {self.email}>'
    def set_password(self, contra):
        self.contra=generate_password_hash(contra)
    def check_password(self, contra):
        return check_password_hash(self.contra, contra)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
    @staticmethod
    def get_all():
        return User.query.all()