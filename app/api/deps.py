from typing import Annotated
from fastapi import Depends, HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from jose import jwt , JWTError
from sqlalchemy.orm import Session 
from app.core.database import SessionLocal
from app.core.config import settings
from app.models.user import User
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
SessionDep = Annotated [ Session, Depends(get_db)]
TokenDep = Annotated [str,Depends(oauth_bearer)]
FormData = Annotated [OAuth2PasswordRequestForm,Depends()]

def get_current_user(token:TokenDep,db:SessionDep):
    cred_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Could not validate user")
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        username:str = payload.get('sub')
        user_id:int = payload.get('id')

        if username is None or user_id is None:
            raise cred_exception
        
        user = db.query(User).filter(User.id == user_id).first()
        return user
    except JWTError:
        raise cred_exception

CurrentUserDep = Annotated[User,Depends(get_current_user)]


