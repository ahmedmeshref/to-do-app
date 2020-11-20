from app import app, db
from app.models import Todo, List
from flask import render_template, request, jsonify, abort, redirect, url_for
import sys


@app.route("/")
def home():
    try:
        lists = db.session.query(List).order_by(List.id).all()
        if not lists:
            print("Running not empty!")
            return render_template('home.html', tasks=[], lists=[], selected_list=None)
        else:
            selected_list = lists[0]
            tasks = db.session.query(Todo).filter(Todo.list_id == selected_list.id).order_by(Todo.id).all()
            return render_template('home.html', tasks=tasks, lists=lists, selected_list=selected_list)
    except Exception as E:
        return abort(500)


@app.route('/l/<list_id>/')
def show_list(list_id):
    # verify a list_id exist
    selected_list = db.session.query(List).get_or_404(list_id)
    try:
        lists = db.session.query(List).order_by(List.id).all()
        tasks = db.session.query(Todo).filter(Todo.list_id == selected_list.id).order_by(Todo.id).all()
        return render_template('home.html', tasks=tasks, lists=lists, selected_list=selected_list)
    except:
        return abort(500)


@app.route("/todos/create", methods=["POST"])
def create_todo():
    body = {}
    error = False
    try:
        json_input = request.get_json()
        description = json_input['description']
        list_id = json_input['list_id']
        if not description:
            return "Value is not valid"
        new_task = Todo(description=description, list_id=list_id)
        db.session.add(new_task)
        db.session.commit()
        body["description"] = new_task.description
        body["id"] = new_task.id
        body["list_id"] = new_task.list_id
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
    try:
        l_name = request.get_json()['list_name']
        new_list = List(name=l_name)
        db.session.add(new_list)
        db.session.commit()
        response = {
            "id": new_list.id,
            "name": new_list.name
        }
    except Exception as E:
        db.session.rollback()
        error = True
    finally:
        db.session.close()

    if not error:
        return jsonify(response)
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
