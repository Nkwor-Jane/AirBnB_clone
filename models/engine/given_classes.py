#!/usr/bin/python
"""
    GIven classes
"""


from ..base_model import BaseModel
from ..user import User
from ..review import Review
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place

check_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Review": Review,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        }

console_mthds = ["all", "create", "show" , "destroy", "update"]

