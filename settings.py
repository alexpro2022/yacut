import os
import string as s

from tests.test_config import WORKFLOW_DATABASE, WORKFLOW_SECRET_KEY

ALPHABET = s.ascii_letters + s.digits
BASE_URL = 'http://localhost'
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


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', WORKFLOW_DATABASE)
    SECRET_KEY = os.getenv('SECRET_KEY', WORKFLOW_SECRET_KEY)
