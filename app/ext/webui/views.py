from flask import abort, render_template
from flask_simplelogin import login_required

from app.models import Object
import random


def index():
    products = Object.query.filter(Object.photo != "").all()
    random.shuffle(products)
    return render_template("index.html", products=products[:10])


def object(product_id):
    product = Object.query.filter_by(id=product_id).first() or abort(
        404, "Такой объект не найден"
    )
    return render_template("product.html", product=product)


@login_required
def secret():
    return "This can be seen only if user is logged in"


@login_required(username="admin")
def only_admin():
    return "only admin user can see this text"
