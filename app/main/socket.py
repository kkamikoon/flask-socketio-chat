import os, random, time

from flask_socketio import emit

from app.socket import socketio


@socketio.on("notify", namespace='/socket/main')
def notify(msg):
    emit(  "announce",
            {   'title'    : msg['title'],
                'desc'     : msg['desc'],
                'category' : msg['category'] },
            namespace='/socket/main',
            broadcast=True)
