from apiflask import APIFlask

def create_app():

    app = APIFlask(__name__)

    @app.get("/")
    def home():
        return "Hello, World!!!"

    return app
if __name__ == "__main__":
    app = create_app()
