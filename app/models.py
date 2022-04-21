# sourcery skip: avoid-builtin-shadow
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from app.ext.database import db


class Object(db.Model, SerializerMixin):
    __tablename__ = "objects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    region = db.Column(db.String())
    unesco = db.Column(db.Boolean())
    photo = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = orm.relation("Category")
    typology_id = db.Column(db.Integer, db.ForeignKey("typologies.id"))
    typology = orm.relation("Typology")

    def __repr__(self):
        return self.name


class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return self.name


class Typology(db.Model, SerializerMixin):
    __tablename__ = "typologies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return self.name


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))


# class Document(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
