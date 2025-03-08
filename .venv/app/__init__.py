from flask import Flask
from flask_login import LoginManager
login_manager=LoginManager()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="holaaaa"
    
    login_manager.init_app(app)
    login_manager.login_view= "login"
    from .public import public_bp
    app.register_blueprint(public_bp)
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    return app