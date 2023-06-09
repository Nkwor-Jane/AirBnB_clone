#!/usr/bin/python3
"""
    Defines User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        class User inherits from Basemodel
    """
    email = " "
    password = " "
    first_name = " "
    last_name = " "

    def __init__(self, *args, **kwargs):
        """ Initialize class """
        super().__init__(*args, **kwargs)
