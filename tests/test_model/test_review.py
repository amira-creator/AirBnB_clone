#!/usr/bin/python3
"""Unittest module That review_class"""

from models.base_model import BaseModel
from models.review import Review
import unittest
import os


class Test_review(unittest.TestCase):
    """Class that tests review"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.review = Review()
        cls_instance.review.place_id = "MA"
        cls_instance.review.user_id = "HAN-13"
        cls_instance.review.text = "5 Star"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that tests functions"""

        self.assertIsNotNone(Review.__doc__)

    def test_save(self):
        """Function that tests saving to json file"""

        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """Fuction that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
