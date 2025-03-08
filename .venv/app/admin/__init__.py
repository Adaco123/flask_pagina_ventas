from flask import Blueprint

admib_bp=Blueprint('admin', __name__, template_folder='templates')
from . import routes
