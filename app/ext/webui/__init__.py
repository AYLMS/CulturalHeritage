from flask import Blueprint

from .views import index, only_admin, object, secret

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/object/<product_id>", view_func=object, endpoint="productview")
bp.add_url_rule("/secret", view_func=secret, endpoint="secret")
bp.add_url_rule("/only_admin", view_func=only_admin, endpoint="onlyadmin")


def init_app(app):
    app.register_blueprint(bp)
