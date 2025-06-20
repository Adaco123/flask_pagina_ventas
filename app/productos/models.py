from flask_sqlalchemy import SQLAlchemy
from app import db
db = SQLAlchemy()

class CarouselImage(db.Model):
    __tablename__ = 'imagenes'

    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)  # ejemplo: "images/carousel/img1.jpg"
    caption = db.Column(db.String(255))
    order = db.Column(db.Integer, default=0)
    visible = db.Column(db.Boolean, default=True)
