#!/usr/bin/python3
"""
    This module define a Base class
"""


import json


class Base:
    """
    This class is the parent class for all the coming classes
    that represent a geometric shape.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            new_list = [obj.__dict__ for obj in list_objs]
            f.write(cls.to_json_string(new_list))
