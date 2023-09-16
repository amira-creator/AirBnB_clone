#!/usr/bin/python3
"""This is unittest module to review_class"""

from models.base_model import BaseModel
from models.review import Review
import unittest
import pep8
import os


class reviewTest(unittest.TestCase):
    """clss for testing review"""

    @classmethod
    def setUp_class(cls_instance):
        """It determine instructions within unittests"""

        cls_instance.review = Review()
        cls_instance.review.place_id = "AS"
        cls_instance.review.user_id = "RUG12"
        cls_instance.review.text = "7_moon"

    @classmethod
    def removeSetUp_class(cls_instance):
        """It removes setup_class"""

        del cls_instance.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    def styleTest(self):
        """this is checking if file is pep8"""

        styleG = pep8.StyleGuide(quiet=True)
        styleCheck = styleG.check_files(['models/review.py'])
        self.assertEqual(styleCheck.total_errors, 0, "fix pep8")

    def subclassTest(self):
        """It tests if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def testDocString(self):
        """It tests functions"""

        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def saveTest(self):
        """it  tests saving to json file"""

        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def to_dictTests(self):
        """It tests dict objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
