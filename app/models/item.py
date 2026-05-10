from typing import List
from sqlalchemy import Column, Integer, String , ForeignKey 
from sqlalchemy.orm import Mapped, Relationship
from app.core.database import Base
from app.models.listing import Listing

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True , nullable=False)
    price = Column(Integer,nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    owner = Relationship("User",secondary="Listing",back_populates="items")
    listing : Mapped[List[Listing]] = Relationship("Listing",back_populates="item")

