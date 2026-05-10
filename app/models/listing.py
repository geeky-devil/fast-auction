from sqlalchemy import Column, Integer, String , ForeignKey ,DateTime
from sqlalchemy.orm import Relationship
from app.core.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer,index= True,primary_key=True)
    seller_id = Column(Integer,ForeignKey("users.id"),nullable= False)
    bidder_id = Column(Integer,ForeignKey("users.id"))
    item_id = Column(Integer,ForeignKey("items.id"),index= True)
    current_bid = Column(Integer,nullable=False)
    created_at = Column(DateTime,nullable=False,index= True)
    expires_at = Column(DateTime,nullable=False,index= True)
    
    item = Relationship("Item",back_populates="listing")
    seller = Relationship("User",back_populates="listing",foreign_keys=seller_id)
    bidder = Relationship("User",back_populates="listing",foreign_keys=bidder_id)
    