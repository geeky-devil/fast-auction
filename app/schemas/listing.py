from datetime import datetime
from pydantic import BaseModel
from app.schemas.item import ItemGet
from app.schemas.user import UserResponse

class ListingBase(BaseModel):
    seller_id:int
    seller_name:str
    top_bidder_id:int | None = None
    current_bid:int

class ListingCreate(BaseModel):
    item_id:int
    current_bid:int

class ListingUpdate(BaseModel):
    id:int
    top_bidder_id:int
    current_bid:int

class ListingGet(BaseModel):
    seller:UserResponse
    item:ItemGet
    top_bidder:UserResponse |None = None
    current_bid:int
    created_at:datetime
    expires_at:datetime
    model_config = {
        'from_attributes':True
    }