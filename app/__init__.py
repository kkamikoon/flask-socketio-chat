import os

from flask import Flask

from app.socket import socketio
from app.utils.initialization import init_template_globals

from app.model import db


def create_app(config="app.config.Config"):
    app = Flask(__name__)
    app.secret_key = app.config.get("SECRET_KEY")

    # Set config
    app.config.from_object(config)

    with app.app_context():
        # Init database
        db.init_app(app)
        db.create_all()

        # Initialization
        init_template_globals(app)

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
