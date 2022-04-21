from sqlalchemy_serializer import SerializerMixin

from app.ext.database import db


class Object(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    region = db.Column(db.String())
    unesco = db.Column(db.String())
    photo = db.Column(db.String())
    createDate = db.Column(db.String())
    category = db.Column(db.String())
    tipology = db.Column(db.String())


class CategoryType(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


class Tipology(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
