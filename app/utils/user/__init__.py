from flask import session

from app.model import db, Users


def get_user():
    name = session.get("name")
    email = session.get("email")

    return Users.query.filter_by(name=name, email=email).one_or_none()


def authed():
    return bool(session.get("name", False))
