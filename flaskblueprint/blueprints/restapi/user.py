import logging

from http import HTTPStatus
from flask import Blueprint, abort, request, jsonify
from marshmallow import ValidationError

from flaskblueprint.models import db, User
from flaskblueprint.schemes import UserAPISchema, CreateUserAPISchema
from flaskblueprint.annotations import login_required

user_blueprint = Blueprint("users", __name__, url_prefix="/users")
logger = logging.getLogger(__name__)


@user_blueprint.route("/", methods=["POST"])
@login_required
def create_user():
    data = request.json

    if not data:
        logger.error("No input data provided")
        return {"message": "No input data provided"}, HTTPStatus.BAD_REQUEST

    try:
        user_info = CreateUserAPISchema().load(data)
        logger.debug(user_info)
    except ValidationError as e:
        logger.error(e.messages)
        return {"error": e.messages}, HTTPStatus.BAD_REQUEST

    if User.query.filter_by(script=user_info["script"]).first():
        logger.debug("User already exists")
        return {"error": "User already exists"}, HTTPStatus.BAD_REQUEST

    user = User(**user_info)
    db.session.add(user)
    db.session.commit()

    return {"message": "User created", "id": user.id}


@user_blueprint.route("/all", methods=["GET"])
@login_required
def get_users():
    try:
        users = User.query.all()
        schema = UserAPISchema(many=True)
        result = schema.dump(users)
        return jsonify(result), 200
    except Exception:
        abort(404, description="Resource not found")


@user_blueprint.route("/<int:id>", methods=["GET"])
@login_required
def get_one_user(id: int):
    try:
        user = User.query.filter_by(id=id).first()
        schema = UserAPISchema()
        result = schema.dump(user)
        return jsonify(result), 200
    except Exception:
        abort(404, description="Resource not found")
