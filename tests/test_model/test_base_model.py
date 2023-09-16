#!/usr/bin/python3
"""This is unittest module for BaseModel class"""

from models.base_model import BaseModel
import unittest
import os
import pep8

class test_base_model(unittest.TestCase):
    """Class to test basemodel"""

    @classmethod
    def setUp_class(cls_instance):
        """determines  instructions within unittests"""

        cls_instance.base = BaseModel()
        cls_instance.base.name = "Helb"
        cls_instance.base.id = 15

    @classmethod
    def remove_setUp_class(cls_instance):
        """removes setup class"""

        del cls_instance.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def styleTest(self):
        """tests if file is pep8"""

        __style = pep8.StyleGuide(quiet=True)
        style_test = __style.check_files(['models/base_model.py'])
        self.assertEqual(style_test.total_errors, 0, "fix pep8")

    def test_docString(self):
        """tests basemodel functions"""

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """Function that tests for attributes in basemodel"""

        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Function to test initializer"""

        self.assertTrue(isinstance(self.base, BaseModel))

    def testSave(self):
        """Function that tests saving of json file"""

        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def to_dict_tests(self):
        """tests dictionary objects of insatnces in basemodel"""

        in_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(in_dict['created_at'], str)
        self.assertIsInstance(in_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
