#!/usr/bin/python3
"""shebang"""
import json
"""imported json module"""


class Base:
    """creste a class named base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        jsonstring = json.dumps(list_dictionaries)
        return jsonstring
