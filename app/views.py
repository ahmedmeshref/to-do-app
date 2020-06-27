from app import app, db
from app.models import Todo
from flask import render_template, request, jsonify, abort
import sys


@app.route('/')
def hello_world():
    tasks = db.session.query(Todo).order_by(Todo.id).all()
    return render_template('home.html', tasks=tasks)


@app.route("/todos/create", methods=["POST"])
def create_todo():
    body = {}
    error = False
    try:
        description = request.get_json()['description']
        if not description:
            return "Value is not valid"
        new_task = Todo(description=description)
        db.session.add(new_task)
        db.session.commit()
        body["description"] = new_task.description
        body["id"] = new_task.id
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        # jsonify transfers an object to a json string
        return jsonify(body)


@app.route("/todos/update_completed", methods=["POST"])
def update_completed():
    error = False
    body = {}
    try:
        id = request.get_json()['id']
        state = request.get_json()['state']
        # get the element from db
        task = db.session.query(Todo).get(id)
        task.completed = state
        db.session.commit()
        body["id"] = task.id
        body["description"] = task.description
        body["state"] = task.completed
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    return abort(500)


@app.route("/todos/<task_id>/delete_task", methods=['POST'])
def delete_task(task_id):
    body = {}
    error = False
    try:
        task = db.session.query(Todo).get(task_id)
        db.session.delete(task)
        db.session.commit()
        body["id"] = task_id
        body["description"] = task.description
        body["state"] = task.completed
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    return abort(500)
