import unittest
from app import create_app, db
from app.auth.models import User

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app=create_app(settings_module="config.testing")
        self.client=self.app.test_client()

        with self.app.app_context():
            db.create_all()
            BaseTestClass.create_user('admin', 'admin@xyz.com', '1111', True)
            # Creamos un usuario invitado
            BaseTestClass.create_user('guest', 'guest@xyz.com', '1111', False)
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    @staticmethod
    def create_user(nombre, email, password, is_admin):
        user = User(nombre, email)
        user.set_password(password)
        user.es_admi= is_admin
        user.save()
        return user
    def login(self, email, password):
        return self.client.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)
    