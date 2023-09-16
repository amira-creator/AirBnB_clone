#!/usr/bin/python3
"""This is unittest module for city class"""

from models.base_model import BaseModel
from models.city import City
import unittest
import pep8
import os


class TestCity(unittest.TestCase):
    """class for testing city"""

    @classmethod
    def class_setup(cls_instance):
        """It determines instructions in unittests"""

        cls_instance.city = City()
        cls_instance.city.name = "Aswan"
        cls_instance.city.state_id = "As"

    @classmethod
    def remove_setup_class(cls_instance):
        """It  removes setup class"""

        del cls_instance.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def testStyle(self):
        """It checks if file is pep8"""

        style_G = pep8.StyleGuide(quiet=True)
        styleTest = style_G.check_files(['models/city.py'])
        self.assertEqual(styleTest.total_errors, 0, "fix pep8")

    def subclassTest(self):
        """it tests if class is subclass in basemodel"""

        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def testDocString(self):
        """ this is for checking functions"""

        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def saveTest(self):
        """This  tests saving of json file"""

        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def to_dictTest(self):
        """This  tests dict obj of instances of  basemodel"""

        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
