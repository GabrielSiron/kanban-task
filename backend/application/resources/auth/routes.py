from apiflask import APIBlueprint
from icecream import ic
from flask import jsonify
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from application.utils.auth_functions import (
    encript_password,
    check_password,
    encode_auth_token,
)

from application.resources.auth.schemas import CreateAccountValidator, LoginValidator

from infrastructure.database import db
from infrastructure.database.entities import User


auth_routes = APIBlueprint("bp_auth", __name__)


@auth_routes.post("/signup")
@auth_routes.input(CreateAccountValidator)
def create_account(json_data):
    if json_data["password"] != json_data["repeat_password"]:
        return jsonify(
            message="Senhas não conferem. Por favor, tente novamente.",
            code=404,
        )

    new_user = User(
        name=json_data["name"],
        email=json_data["email"],
        password=encript_password(json_data["password"]),
    )

    db.session.add(new_user)

    try:
        db.session.commit()
        user_id = (
            db.session.execute(
                select(User.id).where(User.email == new_user.email)
            ).first()
        ).id

        token = encode_auth_token(user_id)
        return jsonify(message="Usuário registrado!", token=token, code=200)

    except IntegrityError as err:
        ic(str(err))
        return jsonify(message="Email já está em uso. Por favor, faça login", code=200)
    finally:
        db.session.close()


@auth_routes.post("/signin")
@auth_routes.input(LoginValidator)
def login(json_data):
    user = User.query.filter_by(email=json_data["email"]).first()

    if user and check_password(json_data["password"], user.password):
        token = encode_auth_token(user.id)
        return jsonify(message="Usuário logado!", token=token, code=200)

    return jsonify(message="Email ou senha incorretos", code=404)
