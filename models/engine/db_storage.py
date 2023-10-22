#!/usr/bin/python3
"""New engine for database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.all_models import our_models
from models.base_model import BaseModel, Base
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review


class DBStorage:
    """database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """init special method
        """
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".
            format(user, passwd, host, db),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create the current database session with expire_on_commit=False
        # session_factory = sessionmaker(
        #     bind=self.__engine, expire_on_commit=False)
        # self.__session = scoped_session(session_factory)

        '''
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        metadata = MetaData(bind=self.__engine)

        if os.getenv("HBNB_ENV") == "test":
            metadata.drop_all()
            self.__session.commit()
        '''

    def all(self, cls=None):
        """query on the current database session (self.__session)
            all objects depending of the class name """

        if cls is not None:
            objs = self.__session.query(cls).all()

        else:
            objs = []
            for _cls in our_models.values():
                objs += self.__session.query(_cls)

        new_dict = {}

        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)

        # Create a session with the specified options
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove method on the private session attribute
        """
        self.__session.remove()
