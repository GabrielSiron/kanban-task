from ...domain.models.auth import check_pw_pattern
from ...app import app
from apiflask import APIFlask, APIBlueprint, abort
from apiflask.exceptions import ValidationError
import bcrypt
from infrastructure.database import db
from infrastructure.database.entities import User
from domain.utils import encript_password, check_password
from domain.validators import CreateAccountValidator, LoginValidator


auth_routes = APIBlueprint("authentications", __name__)

@auth_routes.post("/signup")
@auth_routes.input(CreateAccountValidator)
def create_account(json_data):
    try:
        new_user = User(name=json_data['name'], email=json_data['email'], password=encript_password(json_data['password']))
        db.session.add(new_user)
        db.session.commit()
        return {"message": "Usuário cadastrado com sucesso", "code": 201}
    except ValidationError as err:
        error_messages = err.messages
        return {"message": error_messages, "code": 400}


@auth_routes.post("/signin")
@auth_routes.input(LoginValidator)
def login(json_data):
    user = User.query.filter_by(email=json_data['email']).first()
    if not(user):
        return {"message": "Usuário não encontrado", "code": 401}
    if check_password(json_data['password'], user.password):
            return {"message": "Login bem-sucedido", "code": 200}
    return {"message": "Senha incorreta", "code": 400}