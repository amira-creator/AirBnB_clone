#!/usr/bin/python3
"""Unittest module for User class"""

from models.base_model import BaseModel
from models.user import User
import unittest
import os


class TestUser(unittest.TestCase):
    """Class to test User"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.my_user = User()
        cls_instance.my_user.first_name = "Hannibal"
        cls_instance.my_user.last_name = "Mejbri"
        cls_instance.my_user.email = "hm@test.com"
        cls_instance.my_user.password = "test"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that tests functions"""

        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        """Function that tests saving to json file"""

        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        """Fuction that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
