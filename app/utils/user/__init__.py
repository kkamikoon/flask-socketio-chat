from flask import session

from app.model import db, Users


def get_user():
    user = Users.query.filter_by(idx=session.get("idx")).one_or_none()
    return user


def authed():
    return bool(session.get("name", False))


def my_idx():
    user = Users.query.filter_by(idx=session.get("idx")).one_or_none()
    if user:
        return user.idx
    return ""