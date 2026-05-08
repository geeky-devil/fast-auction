from datetime import datetime
from pydantic import BaseModel

class ListingBase(BaseModel):
    owner_id:int
    top_bidder:str | None = None
    top_bidder_id:int | None = None
    top_bid:int = 0
    minimun_bid:int

class ListingCreate(ListingBase):
    owner_id:int
    minimun_bid:int
    created_at:datetime
    expires_at:datetime

class ListingUpdate(ListingBase):
    id:int
    top_bidder_id:int
    top_bid:int

class ListingGet(ListingBase):
    owner_id:int
    top_bidder:str
    top_bid:int
    minimun_bid:int
    created_at:datetime
    expires_at:datetime
    model_config = {
        'from_attributes':True
    }