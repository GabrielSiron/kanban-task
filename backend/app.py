from apiflask import APIFlask


app = APIFlask(__name__)


def create_app():
    @app.get("/")
    def home():
        return "Hello, World!"


if __name__ == "__main__":
    app = create_app()
