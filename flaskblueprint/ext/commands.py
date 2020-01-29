import click
import logging
from flaskblueprint.ext.database import db
from flaskblueprint.models import User

logger = logging.getLogger(__name__)


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f"{username} ja esta cadastrado")
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    # add a single command
    @app.cli.command()
    @click.option("--username", "-u")
    @click.option("--password", "-p")
    def add_user(username, password):
        """Adds a new user to the database"""
        try:
            return create_user(username, password)
        except Exception:
            logger.error("User alredy exists.")
