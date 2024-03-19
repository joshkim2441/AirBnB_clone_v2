#!/usr/bin/python3
""" Contains TestDBStorage Docs and classes """
import pep8
import inspect
import models
import json
import os
import unittest
import pycodestyle
from datetime import datetime
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """Test documentaton and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Setting up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformanceDb_storage(self):
        """Tests if models/engine/db_storage.py is pep8 compliant"""
        pep8_stl = pep8.StyleGuide(quiet=True)
        res = pep8_stl.check_files(['models.engine/db_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

        def test_pep8_conformanceDb_storage(self):
            """Tests if tests/test_models/test_db_storage.py
            is PEP8 compliant
            """
            pep8_stl = pep8.StyleGuide(quiet=True)
        res = pep8_stl.check_files(['tests/test_models/test_db_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_dbs_function_dcstrngs(self):
        """Test docstring presence in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test Filestorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returnsDict(self):
        """Test if all returns dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_noClass(self):
        """Test all returns all rows when no class passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def testNew(self):
        """Tests if new adds object to database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def testSave(self):
        """Test if save correctly saves objects to file.json"""
