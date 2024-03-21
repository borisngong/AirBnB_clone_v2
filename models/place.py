#!/usr/bin/python3
"""Module for working with the place class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from sqlalchemy.ext.declarative import declarative_base
import shlex


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Represents class for Place inheriting from Basemodel, Base
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """
            Responsible for returning list of reviews.id associated with place
            """
            all_models = models.storage.all()
            reviews_objects = []
            filtered_reviews = []
            for key in all_models:
                review_key = key.replace('.', ' ')
                review_key = shlex.split(review_key)
                if review_key[0] == 'Review':
                    reviews_objects.append(all_models[key])
            for review in reviews_objects:
                if review.place_id == self.id:
                    filtered_reviews.append(review)
            return filtered_reviews

        @property
        def amenities(self):
            """ Responsible for returning list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Responsible for appending amenity ids to the attribute """
            if isinstance(obj, models.Amenity) and \
               obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
