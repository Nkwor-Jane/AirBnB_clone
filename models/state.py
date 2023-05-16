#!/usr/bin/python3
"""
    Defines State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        class State inherits from Basemodel
    """
    name = " "

    def __init__(self, *args, **kwargs):
        """ Initializing State class """
        super().__init__(*args, **kwargs)
