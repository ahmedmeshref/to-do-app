import os


class DefaultConfig(object):
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("IBM_POSTGRESQL") + 'todos'
    # DEBUG = True
