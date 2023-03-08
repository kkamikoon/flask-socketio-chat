from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"

    idx = db.Column(db.String(32), primary_key=True, default=str(uuid4()))
    email = db.Column(db.String(128))
    name = db.Column(db.String(128))
    password = db.Column(db.String(256))

