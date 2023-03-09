from datetime import datetime
from flask import session
from flask_socketio import emit\

from app.model import Users
from app.socket import socketio


@socketio.on("button_click", namespace='/socket/main')
def button_click(msg):
    emit(
        "announce",
        {
            'desc' : msg['desc'],
            'category' : msg['category']
        },
        namespace='/socket/main',
        broadcast=True
    )


@socketio.on("chat_message", namespace='/socket/main')
def chat_message(msg):
    _message = msg.get("message")
    if not _message:
        emit(
            "chat_message",
            {
                "error": "No message!!"
            },
            namespace='/socket/main',
            broadcast=True
        )
    else:
        _user = Users.query.filter_by(email=session.get("email")).one_or_none()
        _time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not _user:
            print(f"No session found.")
            return

        template = (
            f"<div class='direct-chat-msg __chatting_place__'>" +
            f"\n  <div class='direct-chat-infos clearfix'>" +
            f"\n    <span class='direct-chat-name float-left'>{_user.name}</span>" +
            f"\n    <span class='direct-chat-timestamp float-right'>{_time}</span>" +
            f"\n  </div>" +
            f"\n  <img class='direct-chat-img' src='static/img/user1-128x128.jpg' alt='message user image'>" +
            f"\n  <div class='direct-chat-text'>" +
            f"\n    {_message}" +
            f"\n  </div>" +
            f"\n</div>"
        )

        emit(
            "chat_message",
            {
                "template": template,
                "user_idx": session.get("idx"),
                "error": None
            },
            namespace='/socket/main',
            broadcast=True
        )

