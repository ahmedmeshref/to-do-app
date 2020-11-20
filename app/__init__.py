from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.conf import DefaultConfig 

app = Flask(__name__)
# set configurations
app.config.from_object(DefaultConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
