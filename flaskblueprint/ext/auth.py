from flask_simplelogin import SimpleLogin
from flaskblueprint.models import User


def verify_login(user):
    """Check user and password to login"""
    username = user.get("username")
    password = user.get("password")
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if User.verify_hash(password, existing_user.password_hash):
        return True
    return False


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
