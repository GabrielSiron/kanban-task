from flask_testing import TestCase
from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from test.seeder import Seeder
from infrastructure.database import db
from application.resources import user_routes, auth_routes

class BaseTestCase(TestCase):    

    def create_app(self):

        app = APIFlask(__name__)

        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "sqlite:///test_database.db"

        with app.app_context():
            db.init_app(app)
            db.drop_all()
            db.create_all()
            Seeder() # to instantiate a Seeder object populates the database

        app.register_blueprint(user_routes)
        app.register_blueprint(auth_routes)
        
        return app
