from infrastructure.database import db
from infrastructure.database.base import BaseClass


class Tag(db.Model, BaseClass):
    title = db.Column(db.String)
    color = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_relation = db.relationship(
        "User", backref="Tag", foreign_keys=user_id, uselist=False
    ) 