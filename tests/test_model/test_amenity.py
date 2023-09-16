#!/usr/bin/python3
"""This is Unittest modlue for Amenity class"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import pep8
import os


class test_amenity(unittest.TestCase):
    """Class taht tests amenity."""

    @classmethod
    def class_setup(cls_instance):
        """it ddetermine instructions in  unittests"""

        cls_instance.amenity = Amenity()
        cls_instance.amenity.name = "Ball court"

    @classmethod
    def remove_setup_class(cls_instance):
        """It removes setup class."""

        del cls_instance.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def styleTest(self):
        """It checks if file is pep8"""

        style_G = pep8.StyleGuide(quiet=True)
        styleCheck = style_G.check_files(['models/amenity.py'])
        self.assertEqual(styleCheck.total_errors, 0, "fix pep8")

    def subclassTest(self):
        """it tests  if class is subclass of basemodel"""

        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def docStringTest(self):
        """it tests for doc string for func"""

        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.amenity.name), str)

    def saveTest(self):
        """it tests saving of json file"""

        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def to_dictTest(self):
        """ this  tests dict objects of instances of basemodel"""

        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
