from .auth import auth_blueprint
from .user import user_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
