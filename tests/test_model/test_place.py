#!/usr/bin/python3
"""Unittest module for Place class"""

from models.base_model import BaseModel
from models.place import Place
import unittest
import os


class TestPlace(unittest.TestCase):
    """Class to test Place"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.place = Place()
        cls_instance.place.city_id = "MA"
        cls_instance.place.user_id = "13"
        cls_instance.place.name = "Maamoura Coast"
        cls_instance.place.description = "Beach House"
        cls_instance.place.number_rooms = 6
        cls_instance.place.number_bathrooms = 6
        cls_instance.place.max_guest = 6
        cls_instance.place.price_by_night = 50
        cls_instance.place.latitude = 1.3
        cls_instance.place.longitude = 3.1
        cls_instance.place.amenity_ids = []


    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that checks for functions"""

        self.assertIsNotNone(Place.__doc__)

    def test_save(self):
        """Function that tests saving to json file"""

        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """Fuction that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
