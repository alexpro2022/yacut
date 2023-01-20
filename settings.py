import os
# import secrets
# secrets не проходит тесты, хотя все работает


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = os.getenv('SECRET_KEY')  # secrets.token_hex(16)