#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now())
    updated_at = Column(DATETIME, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        if isinstance(self.created_at, datetime):
            dictionary['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """ Delete the current instance from storage """
        models.storage.delete(self)
