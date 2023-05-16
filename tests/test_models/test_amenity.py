#!/usr/bin/python3
"""
    Module for unittests for Amenity class
"""

import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ unittest for Amenity class """
    
    def setUp(self):
        """ Set up method for Amenity class """
        print("setUp")
        self.model = Amenity()

    def tearDown(self):
        """ Tear Down test for Amenity class"""
        print("tearDown")
        self.model = None

    def test_amenity(self):
        """ Test function """
        # object instance of Amenity Class
        obj = Amenity()
        # check if obj is instance of Amenity  and BaseModel class
        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj, BaseModel)
        # check if dictinary contains expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", Amenity.__dict__)
        # check if Amenity class attributes are initialized correctly
        self.assertEqual(obj.name, "")
        self.assertEqual(Amenity.name, "")

if __name__ == "__main__":
    unittest.main()
