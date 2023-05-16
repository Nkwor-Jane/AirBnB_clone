#!/usr/bin/python3
"""
    Module for unittests for User class
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """ unittest for User class """
    
    def setUp(self):
        """ Set up method for User class """
        print("setUp")
        self.model = User()

    def tearDown(self):
        """ Tear Down test for User class"""
        print("tearDown")
        self.model = None

    def test_user(self):
        """ Test function """
        # object instance of User Class
        obj = User()
        # check if obj is instance of User and BaseModel class
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj, BaseModel)
        # check if dictinary contains expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)
        # check if User class attributes are initialized correctly
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name,"")
        self.assertEqual(obj.last_name, "")
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

if __name__ == "__main__":
    unittest.main()
