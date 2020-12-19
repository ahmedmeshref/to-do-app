from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.conf import DefaultConfig 
from flask_login import LoginManager

app = Flask(__name__)
# set configurations
app.config.from_object(DefaultConfig)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
# set the login route when the app tries to access login_required
login_manager.login_view = 'login'
# set a category info to give the login message style
login_manager.login_message_category = 'danger'

from app import views
