from apiflask import APIBlueprint
from infrastructure.database import db
from infrastructure.database.entities import User
from domain.utils import encript_password, check_password
from application.resources.auth.schemas import CreateAccountValidator, LoginValidator


auth_routes = APIBlueprint("bp_auth", __name__)

@auth_routes.post("/signup")
@auth_routes.input(CreateAccountValidator)
def create_account(json_data):
    if User.email_already_in_use(email=json_data["email"]):
        return

    new_user = User(
        name=json_data["name"],
        email=json_data["email"],
        password=encript_password(json_data["password"]),
    )
    db.session.add(new_user)

    try:
        db.session.commit()
        return {"message": "Usuário cadastrado com sucesso", "code": 201}
    except Exception as err:
        error_messages = str(err)
        return {"message": error_messages, "code": 400}


@auth_routes.post("/signin")
@auth_routes.input(LoginValidator)
def login(json_data):
    user = User.query.filter_by(email=json_data["email"]).first()
    if not (user):
        return {"message": "Usuário não encontrado", "code": 401}
    if check_password(json_data["password"], user.password):
        return {"message": "Login bem-sucedido", "code": 200}
    return {"message": "Senha incorreta", "code": 400}
