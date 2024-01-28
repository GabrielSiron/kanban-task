from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Cycle(db.Model, BaseClass):
    title = db.Column(db.String)
    limit_date = db.Column(db.DateTime)

    days = db.relationship('Day', backref='cycle')
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_relation = db.relationship(
        "User", backref="Cycle", foreign_keys=user_id, uselist=False
    )

