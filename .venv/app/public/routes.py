from flask import render_template
from . import public_bp
@public_bp.route("/")
@public_bp.route("/inicio")
def inicio():
    return render_template("base.html")
