#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json



class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        my_dict = {}
        for key, val in FileStorage.__objects.items():
            if isinstance(val,cls):
                my_dict[key] = val
        return my_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                for o in json.load(f).values():
                        name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("File is empty")
        except Exception as e:
            print(f"An error occured: {e}")

    def delete(self, obj=None):
        """ A public instance method to delete obj from __objects"""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()

    def close(self):
        """ A public method that calls reload for
        dserializing the JSON file
        """
        self.reload()
