from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# set the db URI to the postgresql os variable + the db name
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('POSTGRESQL') + "todo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = os.environ.get('SECRETKEY')

db = SQLAlchemy(app)

from app import views
