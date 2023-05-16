#!/usr/bin/python3
"""
    FIleStorage module
"""
import json
from os.path import exists


class FileStorage():
    """
        FileStorage class
        Serializes insance to a JSON file
        Desrializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

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
            sets in __objects the  obj with
            key <obj class name>.id
        """
        dictionary = obj.to_dict()
        k = "{}.{}".format(type(obj).__name__, str(obj.id))
        self.__objects[k] = obj
        self.save()

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dictionary = {}
        for k in self.__objects.keys():
            dictionary[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dictionary))

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        from .given_classes import check_classes
        if exists(self.__file_path) is False:
            return
        try:
            loader = {}
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                loader = json.loads(f)
                for id, dict in loader.items():
                    self.all()[id] = check_classes[dict['__class__']](**dict)
        except Exception as e:
            pass
