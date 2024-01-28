from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Day(db.Model, BaseClass):
    title = db.Column(db.String)
    date = db.Column(db.DateTime)
    
    tasks = db.relationship('Task', backref='user')
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_relation = db.relationship(
        "User", backref="Day", foreign_keys=user_id, uselist=False
    )

    cycle_id = db.Column(db.Integer, db.ForeignKey("cycle.id"))
    cycle_relation = db.relationship(
        "Cycle", backref="Day", foreign_keys=cycle_id, uselist=False
    )
