from datetime import datetime
from pydantic import BaseModel

class Item(BaseModel):
    id:int
    name:str
    price:int

class ItemCreate(BaseModel):
    name:str
    price:int

class ItemGet(BaseModel):
    name:str
    price:int
    model_config = {
        'from_attributes' : True
    }