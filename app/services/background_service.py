from typing import List
from datetime import datetime , timezone
from sqlalchemy.orm import Session
from app.models import Listing , ListingStatus


def clean_up_listing(db:Session):
    now  = datetime.now(timezone.utc)
    listings = db.query(Listing).filter(Listing.expires_at < now,Listing.status == ListingStatus.ACTIVE).all()
    transfer_item_and_mark_expired(listings)
    db.commit()

def transfer_item_and_mark_expired(listings:List[Listing]):
    for l in listings:
        l.status = ListingStatus.EXPIRED
        if l.bidder is not None:
            l.item.owner = l.bidder
            print(f"Item {l.item.name} transfered to {l.bidder.username}")
        print(f"Listing {l.id} expired and closed")
