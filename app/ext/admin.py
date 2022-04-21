from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash

from app.ext.database import db
from app.models import Object, User, Category, Typology

# Proteck admin with login / Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin()


class UserAdmin(sqla.ModelView):
    column_list = ["username"]
    can_edit = False

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


def init_app(app):
    admin.name = "Администрирование"
    admin.template_mode = app.config.FLASK_ADMIN_TEMPLATE_MODE
    admin.init_app(app)

    admin.add_view(sqla.ModelView(Object, db.session, name="Объекты"))
    admin.add_view(sqla.ModelView(Category, db.session, name="Категории"))
    admin.add_view(sqla.ModelView(Typology, db.session, name="Типологии"))
    # admin.add_view(UserAdmin(User, db.session))
