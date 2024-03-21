#!/usr/bin/env python3
"""
Module for working with DBStorage class for interacting with the
SQLAlchemy ORM
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """
    Represents the class that manages database storage operations
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize DBStorage instance, setting up the database engine and
        dropping tables if in 'test' mode
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True
            )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Responsible for querying all objects of a given class from the
        database, or all objects if no class is specified
        """
        objects_dict = {}
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
        else:
            classes = [cls]

        for model_class in classes:
            records = self.__session.query(model_class).all()
            for record in records:
                key = f'{record.__class__.__name__}.{record.id}'
                objects_dict[key] = record

        return objects_dict

    def new(self, obj):
        """
        Responsible for adding a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Responsible for Committing all changes of the current database session
        to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Responsoble for deleting an object from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Responsible for Creating all tables in the database and initialize a
        new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
            )
        self.__session = scoped_session(session_factory)

    def close(self):
        """
        Responsible for closing the current session
        """
        self.__session.close()
