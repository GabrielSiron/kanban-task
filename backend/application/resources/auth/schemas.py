from apiflask import Schema
from apiflask.fields import String
from apiflask.validators import Email, Regexp


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
