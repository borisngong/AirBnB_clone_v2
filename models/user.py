#!/usr/bin/python3
"""Module for intereacting with the user class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """Represents the class for user inheriting from Basenodel, Base
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
