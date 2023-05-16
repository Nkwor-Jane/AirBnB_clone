#!/usr/bin/python3
"""
    FIleStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os.path import exists


class FileStorage:
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
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with
            key <obj class name>.id
        """
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj
        self.save()

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dictionary = {}
        for k in FileStorage.__objects.keys():
            dictionary[k] = FileStorage.__onjects[k].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dictionary))

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if exists(FileStorage.__file_path) is False:
            return
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = {}
                loader = json.load(f)
                for k in loader.keys():
                    cls = loader[k].pop("__class__", None)
                    created = loader[k]["created_at"]
                    created = datetime.strptime(created, "%Y-%m-%d %H:%M:%S.%f")
                    updated = loader[k]["updated_at"]
                    updated = datetime.strptime(updated, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(loader[k])
        except Exception as e:
            pass
