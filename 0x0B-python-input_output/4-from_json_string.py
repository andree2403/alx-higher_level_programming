#!/usr/bin/python3
"""shebang"""

import json
"""imported module"""


def from_json_string(my_str):
    """function that converts from json file"""
    obj = json.loads(my_str)
    return obj
