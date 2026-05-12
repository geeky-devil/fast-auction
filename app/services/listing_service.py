from datetime import datetime, timedelta, timezone
from fastapi import HTTPException , status 
from app.api.deps import CurrentUserDep
from sqlalchemy.orm import Session
from app.models import Listing , User, Item
from app.schemas.listing import *

def get_all(db:Session):
    return db.query(Listing).all()

def get_all_private(user:CurrentUserDep,db:Session):
    return db.query(Listing).filter(Listing.seller_id == user.id).all()
 
def get_listing(*,user:CurrentUserDep,db:Session):
    return []

def create_listing(listing:ListingCreate,user:CurrentUserDep,db:Session):
    exists = db.query(Listing).filter(Listing.item_id == listing.item_id).first()
    if exists:
        raise  HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail= "already listed")
    item = db.query(Item).filter(Item.id == listing.item_id).first() 
    if not item:
        raise  HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail= "item not found")
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
    exists.item = None
    db.delete(exists)
    return {'success':"listing deleted"}

#ddebug route
def remove_all(user:CurrentUserDep,db:Session):
    listings = db.query(Listing).filter(Listing.seller_id == user.id).all()
    for listing in listings:
        listing.item = None
        db.delete(listing)
    db.commit()
    return {'all listings removed'}