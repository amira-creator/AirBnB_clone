#!/usr/bin/python3
"""Unittest module for BaseModel class"""

from models.base_model import BaseModel
import unittest
import os

class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.base = BaseModel()
        cls_instance.base.name = "Hannibal"
        cls_instance.base.id = 13

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc_string(self):
        """Function that tests basemodel functions"""

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save(self):
        """Function that tests saving of json file"""

        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """Function that tests dictionary objects of insatnces in basemodel"""

        in_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(in_dict['created_at'], str)
        self.assertIsInstance(in_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
