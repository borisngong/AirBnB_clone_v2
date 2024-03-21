#!/usr/bin/python3
"""Module for working with the amenity class"""

from sqlalchemy.orm import relationship
from models.place import place_amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Represents the class for Amenity inheriting from Basemodel, Base
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
