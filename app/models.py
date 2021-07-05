from app import db
from flask_login import UserMixin
from app import login_manager


def create_db():
    db.drop_all()
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    lists = db.relationship('List', backref="list",
                            lazy='select', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.id} {self.username}>"


# parent class List which each maps to set of tasks (one to many relationship)
class List(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # set relationship with
    tasks = db.relationship('Todo', backref="list",
                            lazy='select', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<List {self.id} {self.name}>"


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    # foreign key
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id} {self.description}>"
