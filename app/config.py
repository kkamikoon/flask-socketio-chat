import os


class Config(object):
    # Session(Redis) Settings
    SESSION_COOKIE_NAME = "FLASK-SOCKETIO-CHAT-DEMO"
    SESSION_TYPE = "filesystem"
    SECRET_KEY = "FL4Sk-S0CK3TI0-CH4T-D3M0-S3CR3T-K3Y"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///demo.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
