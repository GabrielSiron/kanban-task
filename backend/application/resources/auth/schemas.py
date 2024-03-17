from apiflask import Schema, abort
from apiflask.fields import String, Integer, DateTime
from apiflask.validators import Length, Email, Regexp
from infrastructure.database.entities import User


class CreateAccountValidator(Schema):
    name = String(required=True)
    email = String(required=True, validate=[Email(error="Endereço de email inválido.")])
    password = String(
        required=True,
        validate=Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!#@$%&])", error="Senha fraca"
        ),
    )
    repeat_password = String(required=True)


class LoginValidator(Schema):
    email = String(required=True)
    password = String(required=True)
