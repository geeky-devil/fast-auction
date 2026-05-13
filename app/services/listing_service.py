from datetime import datetime, timedelta, timezone
from app.core.config import settings
from fastapi import HTTPException , status 
from app.api.deps import CurrentUserDep
from sqlalchemy.orm import Session
from app.models import Listing , User, Item ,ListingStatus
from app.schemas.listing import *

def get_all(db:Session):
    return db.query(Listing).all()

def get_all_private(user:CurrentUserDep,db:Session):
    return db.query(Listing).filter(Listing.seller_id == user.id).all()
 
def get_listing(*,user:CurrentUserDep,db:Session):
    return []

def create_listing(listing:ListingCreate,user:CurrentUserDep,db:Session):
    exists = db.query(Listing).filter(Listing.seller_id == user.id).filter(Listing.item_id == listing.item_id, Listing.status == ListingStatus.ACTIVE).first()
    if exists:
        raise  HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail= "already listed")
    item = db.query(Item).filter(Item.id == listing.item_id).first() 
    if not item:
        raise  HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail= "item not found")
    new_listing = Listing(**listing.model_dump())
    new_listing.seller = user
    new_listing.created_at = datetime.now(timezone.utc)
    new_listing.expires_at = datetime.now(timezone.utc) + timedelta(seconds= settings.LISTING_EXPIRE_SECONDS)
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing

def try_bid(bid_req:ListingUpdate,user:CurrentUserDep,db:Session):
    valid_listing = db.query(Listing).filter(Listing.id == bid_req.listing_id).first()
    if not valid_listing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Listing not found")
    
    if user.id == valid_listing.seller_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Stupid, dont bid on your item")
        
    if bid_req.bid_value <= valid_listing.current_bid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail="Bid value should be higher than displayed")
    
    valid_listing.current_bid = bid_req.bid_value
    valid_listing.bidder = user
    db.commit()
    return valid_listing

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