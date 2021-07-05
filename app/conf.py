import os


class DefaultConfig(object):
    SECRET_KEY = os.urandom(32)
    # SQLALCHEMY_DATABASE_URI = os.environ.get("IBM_POSTGRESQL") + 'todos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
