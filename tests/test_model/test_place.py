#!/usr/bin/python3
"""This is  unittest module for Place__class"""

from models.base_model import BaseModel
from models.place import Place
import unittest
import pep8
import os


class Test_place(unittest.TestCase):
    """Class to test Place"""

    @classmethod
    def __setUp_class(cls_instance):
        """ it  determine instructions within unittests"""

        cls_instance.place = Place()
        cls_instance.place.city_id = "Al"
        cls_instance.place.user_id = "15"
        cls_instance.place.name = "Porto Matroh"
        cls_instance.place.description = "Villa"
        cls_instance.place.number_rooms = 4
        cls_instance.place.number_bathrooms = 2
        cls_instance.place.max_guest = 5
        cls_instance.place.price_by_night = 100
        cls_instance.place.latitude = 2.5
        cls_instance.place.longitude = 3.8
        cls_instance.place.amenity_ids = []


    @classmethod
    def remove_setup_class(cls_instance):
        """it removes setup__class"""

        del cls_instance.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    def test_style(self):
        """This is func taht checks if file is pep8"""

        __style = pep8.StyleGuide(quiet=True)
        style_test = __style.check_files(['models/place.py'])
        self.assertEqual(style_test.total_errors, 0, "fix pep8")

    def testSubclass(self):
        """it tests if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def doc_str_Test(self):
        """it  checks for functions"""

        self.assertIsNotNone(Place.__doc__)

    def testAttribute(self):
        """This is tests attributes"""

        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def stringAttribute_test(self):
        """This is to test string attributes"""

        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def testSave(self):
        """It check saving to json file"""

        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def to_dictTest(self):
        """It check dict objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
