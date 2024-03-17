from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Tag(db.Model, BaseClass):
    title = db.Column(db.String)
    color = db.Column(db.String)
    date = db.Column(db.DateTime)
