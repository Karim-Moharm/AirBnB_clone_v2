#!/usr/bin/python3
"""City sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
import os


class City(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"),
                          nullable=False)
        # state = relationship("State", back_populates="cities")

        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
