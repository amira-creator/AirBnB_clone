#!/usr/bin/python3
"""This is unittest module for user_class"""

from models.base_model import BaseModel
from models.user import User
import unittest
import os
import pep8


class test_user(unittest.TestCase):
    """This is class to test User"""

    @classmethod
    def set_up_class(cls_instance):
        """Func determine instructions of  unittests"""

        cls_instance.my_user = User()
        cls_instance.my_user.first_name = "Amira"
        cls_instance.my_user.last_name = "Alx"
        cls_instance.my_user.email = "nm@tests.com"
        cls_instance.my_user.password = "tst"

    @classmethod
    def remove_setUp_class(cls_instance):
        """Function deletes setup class"""

        del cls_instance.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def testStyle(self):
        """Function for checking file is pep8"""

        __styleG = pep8.StyleGuide(quiet=True)
        style_test = __styleG.check_files(['models/user.py'])
        self.assertEqual(style_test.total_errors, 0, "fix pep8")

    def subclassTest(self):
        """ checks if class is subclass of basemodel"""

        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def docString_tests(self):
        """ tests functions"""

        self.assertIsNotNone(User.__doc__)

    def testAttribute(self):
        """This is for testing attributes"""

        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_string_attributes(self):
        """This is for testing string attributes"""

        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def testSave(self):
        """ tests saving to json file"""

        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def testToDict(self):
        """Fuction tests dict obj of instances of  basemodel"""

        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
