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
