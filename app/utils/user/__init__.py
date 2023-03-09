from flask import session

from app.model import db, Users


def get_user():
    user = Users.query.filter_by(idx=session.get("idx")).one_or_none()
    return user


def authed():
    return bool(session.get("name", False))
