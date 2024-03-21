#!/usr/bin/python3
"""Module for interacting with the state class"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Represents  the class for State inheriting from Basemodel, Base
    Attributes:
        name: The state's name.
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all_entities = models.storage.all()
        city_entities = []
        filtered_cities = []
        for key, entity in all_entities.items():
            if key.startswith('City'):
                city_entities.append(entity)
        for city in city_entities:
            if city.state_id == self.id:
                filtered_cities.append(city)
        return filtered_cities
