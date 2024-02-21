from apiflask import APIFlask
from infrastructure.database import db
from infrastructure.database.entities import User
from flask_migrate import Migrate
from flask_cors import CORS

        
def commit(session, commit_fn, close_fn, rollback_fn):
    def _commit(*args):

        success = True
        error_message = ''
        print(args)

        try:
            commit_fn()
        except Exception as e:
            error_message = str(e).split('\n')[0]
            success = False
            rollback_fn()
        finally:
            close_fn()
            
        return success, error_message
    
    return _commit

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
        db.session.commit = commit(db.session, db.session.commit, db.session.close, db.session.rollback)

    @app.get("/")
    def home():
        result = User.query.all()
        return f"Hello, World!!! {str(result)}"

    return app
if __name__ == "__main__":
    app = create_app()
