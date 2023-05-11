#!/usr/bin/python3
"""
Defines the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        Defines all common attributes for other classes
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
            Instantiates all public instance attributes
            Recreate an instance with the dictionary representation
        """
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    time = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, time)
                elif k != "__class__":
                    setattr(self, k, v)
#        else:
#            self.id = str(uuid4())
#           self.created_at = datetime.now()
#           self.updated_at = datetime.now()

    def __str__(self):
        """
            Print [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = type(self).__name__
        return_str = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return (return_str)

    def save(self):
        """
            Updates with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns dictionary containing all values of __dict__
            time must be in ISO format - YYYY-MM-DD
        """
        dict_save = {}
        time_format = datetime.isoformat
        for k in self.__dict__:
            v = self.__dict__[k]
            if k == "created_at" or k == "updated_at":
                dict_save[k] = str(time_foramt(v))
            else:
                dict_save[k] = v
        dict_save["class"] = type(self).__name__
        return dict_save
