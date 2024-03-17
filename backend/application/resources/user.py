from apiflask import APIBlueprint, abort

from infrastructure.database.entities import User

router = APIBlueprint("transaction", __name__)


@router.get("/user/<id>")
def get_user(id):
    user = User.query.filter_by(id=id).first()
    return {"name": user.name}
