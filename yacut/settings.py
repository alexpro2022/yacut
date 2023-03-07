import os
import string as s

ALPHABET = s.ascii_letters + s.digits
HOST = os.getenv('HOST', 'localhost')
BASE_URL = f'http://{HOST}'
PORT = '5000'
CUSTOM_ID_SIZE_AUTO = 6
CUSTOM_ID_SIZE_MANUAL = 16
LINK_SIZE_MAX = 256
LINK_SIZE_MIN = 10
API_ORIGINAL_REQUEST = 'url'
API_SHORT_REQUEST = 'custom_id'
API_ORIGINAL_RESPONSE = 'url'
API_SHORT_RESPONSE = 'short_link'
FORM_ORIGINAL = 'original_link'
FORM_SHORT = 'custom_id'
a_zA_Z0_9 = r'[a-zA-Z0-9]+'
DEFAULT_DATABASE = 'sqlite:///db.sqlite3'
DEFAULT_SECRET_KEY = 'qwerty'
DEFAULT_APP = 'yacut'
DEFAULT_ENV = 'development'


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', DEFAULT_DATABASE)
    SECRET_KEY = os.getenv('SECRET_KEY', DEFAULT_SECRET_KEY)
    FLASK_APP = os.getenv('FLASK_APP', DEFAULT_APP)
    FLASK_ENV = os.getenv('FLASK_ENV', DEFAULT_ENV)
