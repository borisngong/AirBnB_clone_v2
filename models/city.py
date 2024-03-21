#!/usr/bin/python3
"""Module for working with the city class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """Represents the class for City inheriting from Basemodel, Base
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
