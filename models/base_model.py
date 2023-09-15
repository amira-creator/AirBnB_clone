#!/usr/bin/python3
"""Module determines  BaseModel class and all instances"""

from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel:
    """Class determines  BaseModel for Airbnb_clone"""

    def __init__(self, *args, **kwargs):
        """Function that initializes instance public attributes"""

        if kwargs is not None and kwargs != {}:
            for a in kwargs:
                if a == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

                elif a == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

                else:
                    self.__dict__[a] = kwargs[a]

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """it  returns official string rep of instances"""

        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """it  updates public  instance attributes of current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """it returns a dict with key/value pairs of instances"""

        newDict = self.__dict__.copy()
        newDict["__class__"] = type(self).__name__
        newDict["created_at"] = newDict["created_at"].isoformat()
        newDict["updated_at"] = newDict["updated_at"].isoformat()
        return (newDict)
