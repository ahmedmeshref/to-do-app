from decouple import config

class DefaultConfig(object):
    SQLALCHEMY_DATABASE_URI = config("POSTGRESQL") + 'todo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_ECHO = True 
    SECRET_KEY = config("SECRET_KEY")