from .auth import auth_blueprint
from .task import task_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(task_blueprint)
