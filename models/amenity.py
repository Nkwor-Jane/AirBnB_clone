#!/usr/bin/python3
"""
    Defines Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        class Amenity inherits from Basemodel
    """
    name = " "

    def __init__(self, *args, **kwargs):
        """ Initialize Amentiy class """
        super().__init__(*args, **kwargs)
