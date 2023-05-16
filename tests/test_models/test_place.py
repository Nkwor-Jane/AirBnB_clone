#!/usr/bin/python3
"""
    Module for unittests for Place class
"""

import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """ unittest for Place class """
    
    def setUp(self):
        """ Set up method for Place class """
        print("setUp")
        self.model = Place()

    def tearDown(self):
        """ Tear Down test for Place class"""
        print("tearDown")
        self.model = None

    def test_place(self):
        """ Test function """
        # object instance of Place Class
        obj = Place()
        # check if obj is instance of Place and BaseModel class
        self.assertIsInstance(obj, Place)
        self.assertIsInstance(obj, BaseModel)
        # check if dictinary contains expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("city_id", Place.__dict__)
        self.assertIn("user_id", Place.__dict__)
        self.assertIn("name", Place.__dict__)
        self.assertIn("description", Place.__dict__)
        self.assertIn("number_rooms", Place.__dict__)
        self.assertIn("number_bathrooms", Place.__dict__)
        self.assertIn("max_guest", Place.__dict__)
        self.assertIn("price_by_night", Place.__dict__)
        self.assertIn("latitude", Place.__dict__)
        self.assertIn("longitude", Place.__dict__)
        self.assertIn("amenity_ids", Place.__dict__)
        # check if User class attributes are initialized correctly
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name,"")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest,0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms,0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

if __name__ == "__main__":
    unittest.main()
