#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import models
import uuid


Base = declarative_base()


class BaseModel:
    """
    Base class for all models in the HBNB clone.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if not self.id:
            self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """
        Responsible for saving the instance to the database.

        Returns:
            None
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """
        Responsible for deleteing the instance from the database

        Returns:
            None
        """
        models.storage.delete(self)

    def to_dict(self):
        """
        Responsible for Returning a dictionary representation of
        the instance

        Returns:
            dict: Dictionary representation of the instance.
        """
        dict_rep = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                dict_rep[key] = value
        dict_rep['__class__'] = self.__class__.__name__
        if 'created_at' in dict_rep:
            dict_rep['created_at'] = dict_rep['created_at'].isoformat()
        if 'updated_at' in dict_rep:
            dict_rep['updated_at'] = dict_rep['updated_at'].isoformat()
        return dict_rep

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
