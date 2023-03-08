import os

from flask import (
    Flask,
    request,
    session,
    redirect,
    url_for,
    abort,
    render_template,
    flash
)
from app.socket import socketio


def create_app(config="app.config.Config"):
    app = Flask(__name__)

    # Set config
    app.config.from_object(config)

    with app.app_context():
        # SocketIO set up
        # socketio.init_app(
        #     app,
        #     async_mode="eventlet",
        #     cors_allowed_origins="*",
        #     logger=True,
        #     engineio_logger=True
        # )
        socketio.init_app(app, cors_allowed_origins="*")

        from app.main import main

        app.register_blueprint(main)
        
        return app
