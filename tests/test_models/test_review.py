#!/usr/bin/python3
"""
    Module for unittests for Review class
"""

import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """ unittest for Review class """
    
    def setUp(self):
        """ Set up method for Review class """
        print("setUp")
        self.model = Review()

    def tearDown(self):
        """ Tear Down test for Review class"""
        print("tearDown")
        self.model = None

    def test_Review(self):
        """ Test function """
        # object instance of Review Class
        obj = Review()
        # check if obj is instance of Review and BaseModel class
        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj, BaseModel)
        # check if dictinary contains expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)
        self.assertIn("text", Review.__dict__)
        # check if User class attributes are initialized correctly
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text,"")
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

if __name__ == "__main__":
    unittest.main()
