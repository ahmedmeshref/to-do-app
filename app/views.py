from app import app, db
from app.models import Todo, List
from flask import render_template, request, jsonify, abort, redirect, url_for
import sys


@app.route("/")
def home():
    first_list = db.session.query(List).first()
    return redirect(url_for("show_list", list_id=first_list.id))


@app.route('/l/<list_id>/')
def show_list(list_id):
    # try:
    lists = db.session.query(List).order_by(List.id).all()
    selected_list = db.session.query(List).get(list_id)
    tasks = db.session.query(Todo).filter(Todo.list_id == selected_list.id).order_by(Todo.id).all()
    return render_template('home.html', tasks=tasks, lists=lists, selected_list=selected_list)
    # except:
    #     return abort(500)


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
    if not error:
        return jsonify(body)
    return abort(500)


@app.route("/todos/<task_id>/update_completed", methods=["POST"])
def update_completed(task_id):
    error = False
    body = {}
    try:
        task_id = task_id
        state = request.get_json()['state']
        # get the element from db
        task = db.session.query(Todo).get(task_id)
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


@app.route("/todos/<task_id>/delete_task", methods=['DELETE'])
def delete_task(task_id):
    body = {}
    error = False
    try:
        task = db.session.query(Todo).get(task_id)
        db.session.delete(task)
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


@app.route("/todos/create_list", methods=["POST"])
def create_list():
    error = False
    body = {}
    try:
        list_name = request.get_json()['list_name']
        list_item = List(name=list_name)
        db.session.add(list_item)
        db.session.commit()
        body['id'] = list_item.id
        body['name'] = list_item.name
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    return abort(500)


@app.route("/todos/<list_id>/delete_list", methods=['DELETE'])
def delete_list(list_id):
    body = {}
    error = False
    try:
        list_item = db.session.query(List).get(list_id)
        db.session.delete(list_item)
        db.session.commit()
        body["id"] = list_item.id
        body["name"] = list_item.name
    except:
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return body
    return abort(404)
