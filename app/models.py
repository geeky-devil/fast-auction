from typing import List
from sqlalchemy import Column, Integer, String , ForeignKey ,DateTime
from sqlalchemy.orm import Mapped, Relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer,index= True,primary_key=True)
    seller_id = Column(Integer,ForeignKey("users.id"),nullable= False)
    bidder_id = Column(Integer,ForeignKey("users.id"))
    item_id = Column(Integer,ForeignKey("items.id"),index= True)
    current_bid = Column(Integer,nullable=False)
    created_at = Column(DateTime(timezone=True),nullable=False,index= True)
    expires_at = Column(DateTime(timezone=True),nullable=False,index= True)
    
    item = Relationship("Item",back_populates="listing")
    seller = Relationship("User",back_populates="listing",foreign_keys=[seller_id])
    bidder = Relationship("User",foreign_keys=[bidder_id])
    
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True , nullable=False)
    price = Column(Integer,nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    owner = Relationship("User",back_populates="items")
    listing : Mapped[List[Listing]] = Relationship(Listing,back_populates="item")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable=False)
    email = Column(String)
    items : Mapped[List[Item]] = Relationship("Item",back_populates="owner")
    listing  = Relationship(Listing,back_populates="seller",foreign_keys=[Listing.seller_id])
    