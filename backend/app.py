from apiflask import APIFlask
from infrastructure.database import db
from infrastructure.database.entities import User


def create_app():

    app = APIFlask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///database.db"

    with app.app_context():
        db.init_app(app)
        db.create_all()

    @app.get("/")
    def home():
        result = User.query.all()
        return f"Hello, World!!! {str(result)}"

    return app
if __name__ == "__main__":
    app = create_app()
