from app import app, db
from app.models import Todo
from flask import render_template


@app.route('/')
def hello_world():
    return render_template('home.html', data=db.session.query(Todo).all())
