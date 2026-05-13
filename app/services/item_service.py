from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from app.schemas.item import *
from app.core.models import Item


def get_all(user_id:int,db:Session):
    return db.query(Item).filter(Item.owner_id == user_id).all()

def get_item(user_id:int,item_id:int,db:Session):
    item = db.query(Item).filter(Item.owner_id == user_id).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail="item not found")
    return item

def add_item(user_id:int,item:ItemCreate,db:Session):
    new_item = Item(name = item.name, price = item.price , owner_id = user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item