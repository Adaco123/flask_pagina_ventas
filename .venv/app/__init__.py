from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()
login_manager=LoginManager()
def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object(settings_module)

    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True) 
    
    login_manager.init_app(app)
    login_manager.login_view= "login"
    db.init_app(app)
    from .public import public_bp
    app.register_blueprint(public_bp)
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    return app