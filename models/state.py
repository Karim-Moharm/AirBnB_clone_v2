#!/usr/bin/python3
"""State sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        # relationsip is one (State) to many (City)
        cities = relationship('City', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter attribute that returns a list of City instances
            with state_id equal to the current State.id
            """
            city_lst = []

            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    city_lst.append(city)
            return city_lst
