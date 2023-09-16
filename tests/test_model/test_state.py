#!/usr/bin/python3
"""Unittest module for State class"""

from models.base_model import BaseModel
from models.state import State
import unittest
import os

class TestState(unittest.TestCase):
    """Class to test State"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.state = State()
        cls_instance.state.name = "NBO"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that tests for functions"""

        self.assertIsNotNone(State.__doc__)
    def test_save(self):
        """Function that tests saving to json file"""

        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Fuction that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
