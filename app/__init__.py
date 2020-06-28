from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
# set the db URI to the postgresql os variable + the db name
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('POSTGRESQL') + "todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG'] = True
# allow me to see sql query that sqlalchemy runs in the background
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = os.environ.get('SECRETKEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
