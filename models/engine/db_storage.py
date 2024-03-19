#!/usr/bin/python3
""" Defines the DBStorage engine """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User

user = os.getenv('NBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')

classes = {"Amenity": Amenity, "Review": Review, "Place": Place,
            "State": State, "City": City, "User": User}


class DBStorage:
    """ Representation of a database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """ The class DBStorage constructor """
        DB_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pwd, host, db
        )
        self.__engine = create_engine(DB_URL, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method to return a dictionary of objects """
        newDict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    newDict[key] = obj
        return (newDict)

    def new(self, obj):
        """ Inserts the object to current database session """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def delete(self, obj=None):
        """ Removes an object from database storage """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete(
                synchronize_session=False
            )

    def reload(self):
        """ Create current database session """
        Base.metadata.create_all(self.__engine)
        Sess_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        self.__session = scoped_session(Sess_factory)()

    def save(self):
        """ Commit the session changes to the database """
        self.__session.commit

    def close(self):
        """ Close the storage engine """
        self.__session.close()
