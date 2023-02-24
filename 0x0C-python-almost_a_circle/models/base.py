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

    @classmethod
    def save_to_file(cls, list_objs):
        """save the json string to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = []
                for items in list_objs:
                    dict_list.append(items.to_dictionary())
                f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        Args:
            json_string: a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """dictionary to instance"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """load the json file and return instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                if filename is None:
                    return "[]"
                else:
                    list_dicts = base.from_json_string(jsonfile.read())
                    return [cls.create(**d) for d in list_dicts]
