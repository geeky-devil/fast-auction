from datetime import datetime , timedelta
from app.core.config import settings
from pwdlib import PasswordHash
from jose import jwt, JWTError

PasswordHasher = PasswordHash.recommended()

def hash_password(plain) -> str:
    return PasswordHasher.hash(plain)

def verify_password(plain,hashed) ->str:
    return PasswordHasher.verify(plain,hashed)

def create_access_token(username:str, user_id:int,expires_delta:timedelta|None = None):
    to_encode = {'sub':username,'id':user_id}
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expires})

    encoded = jwt.encode(to_encode,key = settings.SECRET_KEY,algorithm = settings.ALGORITHM)
    return encoded

