from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()
login_manager=LoginManager()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="holaaaa"
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:adalid123@localhost:5432/miBaseDeDatos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 
    
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