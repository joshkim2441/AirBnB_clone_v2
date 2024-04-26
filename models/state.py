#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import ForeignKey


class State(BaseModel, Base):
    """ Representation of a State class """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """ A getter attr that returns the City list """
            from models import storage
            city_list = []
            listed_cities = storage.all(City).values()
            for city in listed_cities:
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
