#!/usr/bin/python3
"""This is unittest module for state_class"""

from models.base_model import BaseModel
from models.state import State
import unittest
import os
import pep8

class test_state(unittest.TestCase):
    """This class to test State"""

    @classmethod
    def class_set_up(cls_instance):
        """It determine instructions within unittests"""

        cls_instance.state = State()
        cls_instance.state.name = "EG"

    @classmethod
    def remove_Class_setUp(cls_instance):
        """This is function removes setup class"""

        del cls_instance.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    def test_style(self):
        """Function to check if file is pep8"""

        __style = pep8.StyleGuide(quiet=True)
        style_test = __style.check_files(['models/state.py'])
        self.assertEqual(style_test.total_errors, 0, "fix pep8")

    def testSubclass(self):
        """This is function that checks if class is subclass of basemodel"""

        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def testDocString(self):
        """This is func tests for functions"""

        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_doc_string(self):
        """Function that tests for functions"""

        self.assertIsNotNone(State.__doc__)

    def testSave(self):
        """This is func tests saving to json file"""

        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def to_dict_tests(self):
        """This is func tests dict obj of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
