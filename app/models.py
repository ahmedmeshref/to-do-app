from app import db


# parent class List which each maps to set of tasks (one to many relationship)
class List(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # set relationship with
    tasks = db.relationship('Todo', backref="list", lazy='select', cascade='all, delete-orphan')

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


db.create_all()
