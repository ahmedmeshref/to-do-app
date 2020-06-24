from app import app, db
from app.models import Todo
from app.utils import validate_input
from flask import render_template, request, jsonify, abort
import sys


@app.route('/')
def hello_world():
    return render_template('home.html', data=db.session.query(Todo).all())


@app.route("/todos/create", methods=["POST"])
def create_todo():
    body = {}
    error = False
    try:
        description = request.get_json()['description']
        if not validate_input(description):
            return "Value is not valid"
        new_task = Todo(description=description)
        db.session.add(new_task)
        db.session.commit()
        body["description"] = new_task.description
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        # jsonify transfers an object to a json string
        return jsonify(body)
