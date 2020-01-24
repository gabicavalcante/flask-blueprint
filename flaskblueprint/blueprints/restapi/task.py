import logging

from http import HTTPStatus
from flask import Blueprint, abort, request, jsonify
from marshmallow import ValidationError

from flaskblueprint.models import db, Task
from flaskblueprint.schemes import TaskAPISchema, TaskResposeSchema
from flaskblueprint.annotations import login_required

task_blueprint = Blueprint("tasks", __name__, url_prefix="/tasks")
logger = logging.getLogger(__name__)


@task_blueprint.route("/", methods=["POST"])
@login_required
def create_task():
    data = request.json

    if not data:
        logger.error("No input data provided")
        return {"message": "No input data provided"}, HTTPStatus.BAD_REQUEST

    try:
        task_info = TaskAPISchema().load(data)
        logger.debug(task_info)
    except ValidationError as e:
        logger.error(e.messages)
        return {"error": e.messages}, HTTPStatus.BAD_REQUEST

    if Task.query.filter_by(script=task_info["script"]).first():
        logger.debug("Task already exists")
        return {"error": "Task already exists"}, HTTPStatus.BAD_REQUEST

    task = Task(**task_info)
    db.session.add(task)
    db.session.commit()

    return {"message": "Task created", "id": task.id}


@task_blueprint.route("/all", methods=["GET"])
@login_required
def get_tasks():
    try:
        tasks = Task.query.all()
        schema = TaskResposeSchema(many=True)
        result = schema.dump(tasks)
        return jsonify(result), 200
    except Exception:
        abort(404, description="Resource not found")


@task_blueprint.route("/<int:id>", methods=["GET"])
@login_required
def get_one_task(id: int):
    try:
        task = Task.query.filter_by(id=id).first()
        schema = TaskResposeSchema()
        result = schema.dump(task)
        return jsonify(result), 200
    except Exception:
        abort(404, description="Resource not found")
