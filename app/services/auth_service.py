import app.models as Models
from fastapi import HTTPException, status
from app.api.deps import SessionDep , FormData , TokenDep
from app.core.security import verify_password


def authenticate_user(username:str,password:str,db:SessionDep):
    user = db.query(Models.User).filter(Models.User.username == username).first()
    if not user:
        return False
    if not verify_password(password,user.password):
        return False
    return user

