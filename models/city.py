#!/usr/bin/python3
"""
    Defines City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        class City inherits from Basemodel
    """
    state_id = " "
    name = " "

    def __init__(self, *args, **kwargs):
        """ Initialize City class """
        super().__init__(*args, **kwargs)
