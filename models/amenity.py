#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """ Representation of an amenity data set """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False
                  ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
