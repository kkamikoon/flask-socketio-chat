from flask import session
from flask import current_app as app


def signin_user(user):
    # check duplication
    # app.session_interface.duplication(user)

    session["name"] = user.name
    session["email"] = user.email


def signout_user():
    # Delete from client
    session.clear()
