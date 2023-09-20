#!/usr/bin/python3
"""State sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    # relationsip is one (State) to many (City)
    cities = relationship('City', backref='state',
                          cascade="all, delete, save-update")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        Getter attribute that returns a list of City instances
        with state_id equal to the current State.id
        """

        from models import storage
        lst = []

        for city in storage.all(City).values():
            if self.id == city.state_id:
                lst.append(city)
        return lst
