from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Day(db.Model, BaseClass):
    date = db.Column(db.DateTime)
    tasks = db.relationship("Task", backref="user", overlaps="tasks,user")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    cycle_id = db.Column(db.Integer, db.ForeignKey("cycle.id"))