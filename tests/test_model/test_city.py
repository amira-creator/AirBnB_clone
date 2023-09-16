#!/usr/bin/python3
"""Unittest module for City class"""

from models.base_model import BaseModel
from models.city import City
import unittest
import os


class TestCity(unittest.TestCase):
    """Class to test City"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.city = City()
        cls_instance.city.name = "Maamoura"
        cls_instance.city.state_id = "MA"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Function that checks if class is subclass of basemodel"""

        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that checks functions"""

        self.assertIsNotNone(City.__doc__)

    def test_save(self):
        """Function that tests saving of json file"""

        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Function that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
