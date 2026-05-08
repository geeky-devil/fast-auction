from typing import List , Optional 
from sqlalchemy.orm import Relationship , Mapped
from sqlalchemy import Column, Integer, String
from app.core.database import Base
from app.models.item import Item

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable=False)
    email = Column(String)
    items : Mapped[List["Item"]] = Relationship("Item",back_populates= "owner")