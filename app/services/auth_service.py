from app.core.models import User
from fastapi import HTTPException, status
from app.core.deps import SessionDep , FormData , TokenDep
from app.core.security import verify_password


def authenticate_user(username:str,password:str,db:SessionDep):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password,user.password):
        return False
    return user

