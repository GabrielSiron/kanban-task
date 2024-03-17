from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from apiflask import abort


db = SQLAlchemy()
