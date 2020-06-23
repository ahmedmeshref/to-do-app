from app import app, db
from app.models import Todo
from app.utils import validate_input
from flask import render_template, request, jsonify


@app.route('/')
def hello_world():
    return render_template('home.html', data=db.session.query(Todo).all())


@app.route("/add_task", methods=["POST"])
def add_task():
    description = request.get_json()['description']
    try:
        if not validate_input(description):
            return "Value is not valid"
        new_task = Todo(description=description)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({
            'description': new_task.description
        })
    except:
        db.session.rollback()

