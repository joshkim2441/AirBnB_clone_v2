#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table

assoc_table = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60),
                           ForeignKey('places.id'),
                           primary_key=True, nullable=False),
                    Column('amenity_id', String(60),
                           ForeignKey('amenities.id'),
                           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != 'db':
        @property
        def reviews(self):
            """ Getter attr that returns list of Review instances """
            rvw_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    rvw_list.append(review)
            return rvw_list

        @property
        def amenities(self):
            """ Getter attr that returns list of Amanity instances """
            amenity_list = []
            for value in models.storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenity_list.append(value)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """ Setter attr that handles append method to
            add an Amenity to the attr amenity_ids
            """
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)
