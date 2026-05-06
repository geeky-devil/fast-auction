import app.models as Models
from app.core.security import PasswordHasher
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate

def get_user(user_id:int,db:Session) -> Models.User:
    user = db.query(Models.User).filter(Models.User.id == user_id).first()
    return user

def create_user(user:UserCreate,db:Session):
    existing = db.query(Models.User).filter(Models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "User already exists")
    
    new_user = Models.User(username = user.username , email = user.email, password = PasswordHasher.hash(user.password)) # model.dump?
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user