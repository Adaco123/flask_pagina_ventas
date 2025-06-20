from os.path import abspath, dirname, join

BASE_DIR=dirname(dirname(abspath(__file__)))
# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

SECRET_KEY='HOLA:MUNDO'

SQLALCHEMY_TRACK_MODIFICATIONS=False
APP_ENV_LOCAL='local'
APP_ENV_TESTING='testing'
APP_ENV_DEVELOPMENT='development'
APP_ENV_STAGING='staging'
APP_ENV_PRODUCTION='production'
APP_ENV = ''
#loggers
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'adalidgarcia753@gmail.com'
MAIL_PASSWORD = 'nctnilqpyhcwiwdm'
DONT_REPLY_FROM_EMAIL = '(Adalid, adalidgarcia753@gmail.com)'
ADMINS = ('adalidgarcia753@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

ITEMS_PER_PAGE = 3