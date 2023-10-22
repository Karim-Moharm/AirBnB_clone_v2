#!/usr/bin/python3
"""module has BaseModule"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import os


storage_type = os.getenv("HBNB_TYPE_STORAGE")

if (storage_type == "db"):
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """BaseModel that defines all common attributes/methods
    for other classes
    """
    if (storage_type == "db"):
        id = Column(String(60), unique=True, primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """init magic method

        Args:
            args: is a Tuple that contains all arguments (unused)
            kwargs:  is a dictionary that contains all arguments by key/value
        """

        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        # if len(kwargs) == 0:
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, dt_format)
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

    def __str__(self):
        """string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of the instance
        """
        _dict = {}
        _dict = self.__dict__.copy()
        _dict['__class__'] = (str(type(self)).split('.')[-1]
                              ).split('\'')[0]
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        _dict.pop("_sa_instance_state", None)
        return _dict

    def delete(self):
        """delete the current instance from the storage
        """
        from models import storage
        storage.delete(self)
