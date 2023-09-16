#!/usr/bin/python3
"""Unittest module for BaseModel class"""

from models.base_model import BaseModel
import unittest
import os


class Test_Base_Model(unittest.TestCase):
    """Class to test BaseModel"""

    @classmethod
    def setUp_Class(cls_instance):
        """it determines instructions for unittests"""

        cls_instance.base = BaseModel()
        cls_instance.base.name = "Helbrton"
        cls_instance.base.id = 30

    @classmethod
    def remove_class(cls_instance):
        """it removes setup class"""

        del cls_instance.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def doc_str_test(self):
        """it tests basemodel functions"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def attribute_test(self):
        """it tests for attributes of  basemodel"""

        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def testInit(self):
        """it tests initializer"""

        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        """it tests saving of json file"""

        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def to_dict_test(self):
        """Function tests dict objects of insatnces of basemodel"""

        dic = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(dic['created_at'], str)
        self.assertIsInstance(dic['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
