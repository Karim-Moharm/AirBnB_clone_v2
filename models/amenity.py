#!/usr/bin/python3
"""Amenity sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenity = relationship("Place", secondary=place_amenity)
    else:
        name = ""
