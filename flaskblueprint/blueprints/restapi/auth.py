import logging

from http import HTTPStatus
from flask import Blueprint, request

from flaskblueprint.models import User


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
logger = logging.getLogger(__name__)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        logger.error("No input data provided")
        return {"error": "No input data provided"}, HTTPStatus.BAD_REQUEST

    username = data["username"]
    password = data["password"]

    current_user = User.query.filter_by(username=username).first()
    if not current_user:
        return {"message": "User {} doesn't exist".format(username)}, 401

    if User.verify_hash(password, current_user.password_hash):
        access_token = current_user.generate_token()
        return {
            "message": "Token to user {} was created".format(data["username"]),
            "token": access_token,
        }

    return {"error": "Invalid Login"}
