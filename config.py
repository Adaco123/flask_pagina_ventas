from flask_sqlalchemy import SQLAlchemy
def PatronSingleton(clase):
    instancia={}
    def envoltura(*args, **kwargs):
        if clase not in instancia:
            instancia[clase]=clase(*args, **kwargs)
        return instancia[clase]
    return envoltura
@PatronSingleton
class SingletonSQLAlchemy(SQLAlchemy):
    pass
# Inicializar SQLAlchemy
db = SingletonSQLAlchemy()

