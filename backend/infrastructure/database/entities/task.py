from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Task(db.Model, BaseClass):
    title = db.Column(db.String)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    day_id = db.Column(db.Integer, db.ForeignKey("day.id"))
