from infrastructure.database import db
from infrastructure.database.base import BaseClass
from sqlalchemy import select


class User(db.Model, BaseClass):
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    cycles = db.relationship("Cycle", backref="user")

    @classmethod
    def email_already_in_use(cls, email=None):
        user = select(cls.email).where(email=email).first()
        return user
