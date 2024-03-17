from infrastructure.database.entities import User, Cycle, Day, Task, Tag
from infrastructure.database import db

from test.data import CYCLES, USERS, TASKS, TAGS, DAYS


class Seeder:
    def __init__(self):
        tags = [Tag(**data) for data in TAGS]
        users = [User(**data) for data in USERS]
        cycles = [Cycle(**data) for data in CYCLES]
        days = [Day(**data) for data in DAYS]
        tasks = [Task(**data) for data in TASKS]

        db.session.add_all(tags)
        db.session.add_all(users)
        db.session.add_all(cycles)
        db.session.add_all(days)
        db.session.add_all(tasks)

        db.session.commit()
        db.session.close()
