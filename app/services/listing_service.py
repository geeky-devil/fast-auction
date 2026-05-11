from datetime import datetime, timedelta, timezone
from fastapi import HTTPException , status 
from app.api.deps import CurrentUserDep
from sqlalchemy.orm import Session
from app.models import Listing , User, Item
from app.schemas.listing import *

def get_all(db:Session):
    return db.query(Listing).all()

def get_listing(*,user:CurrentUserDep,db:Session):
    return []

def create_listing(listing:ListingCreate,user:CurrentUserDep,db:Session):
    item = db.query(Item).filter(Item.owner_id == user.id).filter(Item.id == listing.item_id).first()
    if not item:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail= "Requested item not available")
    new_listing = Listing(**listing.model_dump())
    new_listing.seller = user
    new_listing.created_at = datetime.now(timezone.utc)
    new_listing.expires_at = datetime.now(timezone.utc) + timedelta(minutes=3)
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing

def remove_listing(listing_id,user:CurrentUserDep,db:Session):
    exists = db.query(Listing).filter(listing_id).first()
    if not exists:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT , detail= "Listing does not exist!")
    db.delete(exists)
    return {'success':"listing deleted"}