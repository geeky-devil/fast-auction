from typing import List
from datetime import datetime , timezone
from sqlalchemy.orm import Session
from app.core.helper import DateTimeUTCNow
from app.core.models import Listing , ListingStatus


def resolve_listing(db:Session):
    listings = db.query(Listing).filter(Listing.expires_at < DateTimeUTCNow(),Listing.status == ListingStatus.ACTIVE).all()
    for l in listings:
        transfer_items_mark_expired(l,db)
    db.commit()

def transfer_items_mark_expired(listing:Listing,db:Session):
    listing.status = ListingStatus.EXPIRED
    if listing.bidder is not None:
        print(f'Transfering item {listing.item.name} to {listing.bidder.username},value {listing.current_bid}')
        listing.item.owner = listing.bidder
        db.flush()