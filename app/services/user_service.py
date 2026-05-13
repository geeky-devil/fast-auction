from app.core.models import User
from app.core.security import PasswordHasher
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate

def get_user(user_id:int,db:Session) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    return user

def create_user(user:UserCreate,db:Session):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "User already exists")
    
    new_user = User(username = user.username , email = user.email, password = PasswordHasher.hash(user.password)) # model.dump?
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user