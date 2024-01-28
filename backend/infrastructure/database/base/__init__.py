from sqlalchemy.sql import func

from infrastructure.database import db


class BaseClass:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())