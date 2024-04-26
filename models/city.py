#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, String, ForeignKey, DateTime


class City(BaseModel, Base):
    """ Represents the city class for a MySQL database """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
