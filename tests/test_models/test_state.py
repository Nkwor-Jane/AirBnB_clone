#!/usr/bin/python3
"""
    Module for unittests for State class
"""

import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """ unittest for State class """
    
    def setUp(self):
        """ Set up method for State class """
        print("setUp")
        self.model = State()

    def tearDown(self):
        """ Tear Down test for State class"""
        print("tearDown")
        self.model = None

    def test_state(self):
        """ Test function """
        # object instance of State Class
        obj = State()
        # check if obj is instance of State and BaseModel class
        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj, BaseModel)
        # check if dictinary contains expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", State.__dict__)
        # check if State class attributes are initialized correctly
        self.assertEqual(obj.name, "")
        self.assertEqual(State.name, "")

if __name__ == "__main__":
    unittest.main()
