from app import app
from flask import render_template


@app.route('/')
def hello_world():
    data = [
        {"description": "Build GUI"},
        {"description": "Intialize Repo"},
        {"description": "Finsh html"}
    ]
    return render_template("home.html", data=data)
