import os
import random

from app.socket import socketio

from flask import current_app as app
from flask import Blueprint, render_template, send_file, abort
from flask import send_from_directory

from app.main import socket

main = Blueprint("main", __name__)


@main.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@main.route("/static/<path:path>")
def statics(path):
    print(f"PATH : {path}")
    filename = send_from_directory(app.root_path, "static", path)

    if os.path.isfile(filename):
        return send_file(filename)
    else:
        abort(404)


@main.route("/test", methods=["GET"])
def test():
    categories = ["success", "warning", "error", "default"]
    category = random.choice(categories)

    socketio.emit(
        "announce",
        {
            "desc": f"{category.upper()} toast message is broadcasted.",
            "category": category
        },
        namespace="/socket/main",
        broadcast=True
    )
    return ""