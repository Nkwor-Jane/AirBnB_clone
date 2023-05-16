#!/usr/bin/python3
"""
    Module for unittests for City class
"""

import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TesCityClass(unittest.TestCase):
    """ unittest for City class """
    
    def setUp(self):
        """ Set up method for City class """
        print("setUp")
        self.model = City()

    def tearDown(self):
        """ Tear Down test for City class"""
        print("tearDown")
        self.model = None

    def test_state(self):
        """ Test function """
        # object instance of City Class
        obj = City()
        # check if obj is instance of City and BaseModel class
        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)
        # check if dictinary contains expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", City.__dict__)
        self.assertIn("state_id", City.__dict__)
        # check if City class attributes are initialized correctly
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.state_id, "")
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")

if __name__ == "__main__":
    unittest.main()
