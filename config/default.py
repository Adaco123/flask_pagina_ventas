from os.path import abspath, dirname

BASE_DIR=dirname(dirname(abspath(__file__)))
SECRET_KEY='HOLA:MUNDO'

SQLALCHEMY_TRACK_MODIFICATIONS=False
APP_ENV_LOCAL='local'
APP_ENV_TESTING='testing'
APP_ENV_DEVELOPMENT='development'
APP_ENV_STAGING='staging'
APP_ENV_PRODUCTION='production'
APP_ENV=''