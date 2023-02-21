# Создаю модель для базы данных
from marshmallow import Schema, fields

from app.db_setup import db


# Класс таблицы Frameworks в базе данных
class FrameworkModel(db.Model):
    __tablename__ = 'frameworks'
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    language = db.Column(db.String)


# Класс для сериализации обьектов модели Framework
class FrameworkSchema(Schema):
    pk = fields.Integer(dump_only=True)
    name = fields.String()
    language = fields.String()
