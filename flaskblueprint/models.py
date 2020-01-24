from __future__ import annotations
import jwt
import logging
from datetime import timedelta, datetime
from passlib.hash import pbkdf2_sha256 as sha256
from dynaconf import settings
from flaskblueprint.ext.database import db
from sqlalchemy_serializer import SerializerMixin

logger = logging.getLogger(__name__)


class User(db.Model, SerializerMixin):
    """ User Model for storing details user"""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    created_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(), nullable=False
    )

    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = sha256.hash(password)

    def generate_token(self) -> str:
        """
        Generates auth token using user data
        :return: string
        """
        try:
            payload = {
                "user_data": self.serialize(),
                "exp": datetime.utcnow() + timedelta(minutes=600),
                "iat": datetime.utcnow(),
            }
            token = jwt.encode(
                payload, settings.JWT_SECRET_KEY, algorithm="HS256"
            ).decode("utf-8")
            return token
        except Exception as e:
            logger.error(e)
            return None

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def serialize(self) -> str:
        return {"id": self.id, "username": self.username}


class Task(db.Model):
    """ Task Model form storing details about each task"""

    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(), nullable=False
    )

    def __init__(self, description: str, script: str):
        self.description = description
        self.script = script

    def __repr__(self) -> str:
        return "<Task (description={})>".format(self.description)
