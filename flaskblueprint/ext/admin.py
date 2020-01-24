from flask_admin import Admin, expose
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from flask_admin.model import typefmt
from datetime import datetime

from flaskblueprint.ext.database import db
from flaskblueprint.models import (
    Task,
    User,
)

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


class AdminView(sqla.ModelView):
    def __init__(self, *args, **kwargs):
        super(AdminView, self).__init__(*args, **kwargs)

        self.column_formatters = dict(typefmt.BASE_FORMATTERS)
        self.column_formatters.update(
            {type(None): typefmt.null_formatter, datetime: self.date_format}
        )

        self.column_type_formatters = self.column_formatters

    def date_format(self, view, value):
        return value.strftime("%d %b %Y - %I:%M:%p")


class HomeView(AdminIndexView):
    @expose("/")
    def index(self):
        users_count = User.query.count()
        tasks_count = Task.query.count()
        return self.render(
            "admin/home.html", users_count=users_count, tasks_count=tasks_count,
        )


class UserAdmin(AdminView):
    column_list = ["username"]
    can_edit = False


class TaskView(AdminView):
    page_size = 50


def init_app(app):
    admin = Admin(index_view=HomeView())
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.base_template = "layout.html"
    admin.init_app(app)
    admin.add_view(TaskView(Task, db.session))
    admin.add_view(UserAdmin(User, db.session))
