from flask import Blueprint
producto_bp=Blueprint("productos", __name__, template_folder="templates")
from . import routes