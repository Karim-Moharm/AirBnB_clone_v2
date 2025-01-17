#!/usr/bin/python3
"""user sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        reviews = relationship('Review', backref='user',
                               cascade="all, delete, save-update")
        places = relationship("Place", backref="user",
                              cascade="all, delete, save-update")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """the __init__ special method"""
        super().__init__(*args, **kwargs)

    # def to_dict(self):
    #     """method to return dict representation for the class"""
    #     return super().to_dict()
