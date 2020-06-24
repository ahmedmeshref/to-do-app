from app import app, db
from app.models import Todo
from app.utils import validate_input
from flask import render_template, request, jsonify, abort


@app.route('/')
def hello_world():
    return render_template('home.html', data=db.session.query(Todo).all())


@app.route("/todos/create", methods=["POST"])
def create_todo():
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
    except Exception:
        db.session.rollback()
        return abort(500)
    finally:
        db.session.close()

