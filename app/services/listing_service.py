from fastapi import HTTPException , status
from app.api.deps import CurrentUserDep
from sqlalchemy.orm import Session
from app.models import Listing


def get_all(user:CurrentUserDep,db:Session):
    return db.query(Listing).all()

def get_listing(*,user:CurrentUserDep,db:Session):
    return []