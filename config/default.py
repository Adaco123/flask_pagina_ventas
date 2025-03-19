from os.path import abspath, dirname

BASE_DIR=dirname(dirname(abspath(__file__)))
SECRET_KEY='HOLA:MUNDO'

SQLALCHEMY_TRACK_MODIFICATIONS=False
APP_ENV_LOCAL='local'
APP_ENV_TESTING='testing'
APP_ENV_DEVELOPMENT='development'
APP_ENV_STAGING='staging'
APP_ENV_PRODUCTION='production'
APP_ENV = ''
#loggers
MAIL_SERVER = 'tu servidor smtp'
MAIL_PORT = 587
MAIL_USERNAME = 'garciita753@gmail.com'
MAIL_PASSWORD = 'cabe1A2B3C4D'
DONT_REPLY_FROM_EMAIL = 'dirección from'
ADMINS = ('garciita753@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False