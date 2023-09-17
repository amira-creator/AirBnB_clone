#!/usr/bin/python3
"""File that storages module for AirBnB_clone"""

from datetime import datetime
import json
import os


class FileStorage:
    """Class that stores data from Console."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ it returns all stored objects."""

        return (self.__objects)

    def new(self, obj):
        """ it  sets obj with class_name key."""

        class_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[class_key] = obj

    def save(self):
        """it  saves obj to JSON file."""

        with open(self.__file_path, "w", encoding="utf-8") as an:
            obj = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(obj, an)

    def classes(self):
        """Function that returns dictionary of class instances"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"Amenity": Amenity,
                   "BaseModel": BaseModel,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "User": User,
                   "State": State}
        return (classes)

    def reload(self):
        """Function that deserializes JSON file to __objects."""

        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for
                        k, v in obj_dict.items()}
            self.__objects = obj_dict

    def attributes(self):
        """Function that returns class instances and their attributes"""

        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime,
                      "updated_at": datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return (attributes)
