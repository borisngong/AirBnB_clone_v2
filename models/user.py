#!/usr/bin/python3
"""Module for working with the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

Base = declarative_base()


class User(BaseModel, Base):
    """Represents class for User inheriting from BaseModel, Base
    Attributes:
        __tablename__: name of the table, users
        email: string column with 128 characters, cannot be null
        password: string column with 128 characters, cannot be null
        first_name: string column with 128 characters, can be null
        last_name: string column with 128 characters, can be null
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def places(self):
            """Getter method for places attribute"""
            place_list = []
            for place in list(models.storage.all(Place).values()):
                if place.user_id == self.id:
                    place_list.append(place)
            return place_list

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
