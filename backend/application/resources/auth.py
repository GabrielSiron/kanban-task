from ...domain.models.auth import check_pw_pattern
from ...app import app
from apiflask import APIFlask, APIBlueprint, abort
import bcrypt
from infrastructure.database import db
from infrastructure.database.entities import User

router = APIBlueprint("authentications", __name__)


@router.post("/signup")
@input("name", str)
@input("email", str)
@input("password", str)
def create_account(name, email, password):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"message": "Email já cadastrado", "code": 400}
    elif not (check_pw_pattern(password)):
        return {"message": "Senha fraca", "code": 400}
    else:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "Usuário cadastrado com sucesso", "code": 201}


@router.post("/signin")
@input("email", str)
@input("password", str)
def login(email, password):
    user = User.query.filter_by(email=email).first()
    if not(user):
        return {"message": "Usuário não encontrado", "code": 401}
    if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return {"message": "Login bem-sucedido", "code": 200}
    return {"message": "Senha incorreta", "code": 401}
