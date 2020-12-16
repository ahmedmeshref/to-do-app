import os


class DefaultConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRESQL") + 'todos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    # SQLALCHEMY_ECHO = True 
    SECRET_KEY = os.environ.get("SECRET_KEY")
