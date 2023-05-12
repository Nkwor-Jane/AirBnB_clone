#!/usr/bin/python3
"""
    FIleStorage module
"""
import json
from models.base_model inport BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.places import Places


class FileStorage:
    """
        FileStorage class
        Serializes insance to a JSON file
        Desrializes JSON file to instances
    """
    __file_path = "file.json"
    __objecs = {}

    def __init__(self):
        """
            init method
        """
        pass
    
    def all(self):
        """
            Returns dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with
            key <obj class name>.id
        """
        k = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[k] = obj
        self.save()

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dictionary = {}
        for k, v in self.__objects.items():
            dictionary[k]] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(dumps(dictionary))

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if exists(self.__file_path) is False:
            return
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                loader = json.load(f)

        except Exception as e:
            pass


