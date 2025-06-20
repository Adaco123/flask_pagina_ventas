from . import producto_bp
from flask import render_template
from .models import CarouselImage
@producto_bp.route("/carrusel/")
def carrusel():
    images = CarouselImage.query.filter_by(visible=True).order_by(CarouselImage.order).all()
    return render_template("productos/carrusel.html", images=images)