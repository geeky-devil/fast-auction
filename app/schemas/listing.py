from datetime import datetime
from pydantic import BaseModel

class ListingBase(BaseModel):
    seller_id:int
    seller_name:str
    top_bidder_id:int | None = None
    minimun_bid:int

class ListingCreate(BaseModel):
    seller_id:int
    item_id:int
    minimun_bid:int
    created_at:datetime
    expires_at:datetime

class ListingUpdate(BaseModel):
    id:int
    top_bidder_id:int
    top_bid:int

class ListingGet(BaseModel):
    seller_name:str
    top_bidder:str
    minimun_bid:int
    created_at:datetime
    expires_at:datetime
    model_config = {
        'from_attributes':True
    }