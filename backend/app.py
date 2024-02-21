from apiflask import APIFlask
from infrastructure.database import db
from infrastructure.database.entities import User
from flask_migrate import Migrate
from flask_cors import CORS
from application.resources import auth_routes


def create_app():

    app = APIFlask(__name__)
    migrate = Migrate()
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///database.db"

    
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        db.create_all()

    app.register_blueprint(auth_routes)
    
    @app.get("/")
    def home():
        result = User.query.all()
        return f"Hello, World!!! {str(result)}"

    return app
if __name__ == "__main__":
    app = create_app()
