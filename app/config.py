import os


class Config(object):
    # Session(Redis) Settings
    SESSION_COOKIE_NAME = "FLASK-SOCKETIO-CHAT-DEMO"
    SESSION_TYPE = "redis"
