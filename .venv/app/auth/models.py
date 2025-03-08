from flask_login import UserMixin

users = []

class User(UserMixin):  # Hereda UserMixin para compatibilidad con Flask-Login
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        users.append(self)

    @classmethod
    def get_by_email(cls, email):
        for user in users:
            if user.email == email:
                return user
        return None

    @classmethod
    def get(cls, email):  # Flask-Login puede intentar usar get()
        return cls.get_by_email(email)  # Redirigir a get_by_email()

    # Métodos requeridos por Flask-Login
    def get_id(self):
        return self.email  # Flask-Login usa esto como identificador único

    @property
    def is_active(self):
        return True  # En este caso, todos los usuarios están activos

    @property
    def is_authenticated(self):
        return True  # Si el usuario existe, se considera autenticado

    @property
    def is_anonymous(self):
        return False  # No hay usuarios anónimos en este sistema
