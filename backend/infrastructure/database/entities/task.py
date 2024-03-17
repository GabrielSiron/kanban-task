from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Task(db.Model, BaseClass):
    title = db.Column(db.String)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)

    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
    tag_relation = db.relationship(
        "Tag", backref="Task", foreign_keys=tag_id, uselist=False
    )

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_relation = db.relationship(
        "User", backref="Task", foreign_keys=user_id, uselist=False
    )

    day_id = db.Column(db.Integer, db.ForeignKey("day.id"))
    day_relation = db.relationship(
        "Day", backref="Task", foreign_keys=day_id, uselist=False
    )
