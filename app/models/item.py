from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import Relationship
from app.core.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True , nullable=False)
    price = Column(Integer,nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    owner = Relationship("User",back_populates="items")

