from apiflask import Schema, abort
from apiflask.fields import String, Integer, DateTime
from apiflask.validators import Length, Email, Regexp, Unique
from infrastructure.database.entities import User

class CreateAccountValidator(Schema):
    name = String(required=True)
    email = String(required=True, 
        validate=[
            Email(error="Endereço de email inválido."),
            Unique(model=User, field=User.email, error="Email já cadastrado.")
        ]
    )
    password = String(required=True, validate=Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!#@$%&])', error="Senha fraca"))

class LoginValidator(Schema):
    email = String(required=True)
    password = String(required=True)