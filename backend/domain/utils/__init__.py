from flask import request
import bcrypt

def encript_password(password):
    hashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    return hashed

def check_password(typed_password, user_password):
    return bcrypt.checkpw(typed_password.encode("utf-8"), user_password.encode("utf-8"))