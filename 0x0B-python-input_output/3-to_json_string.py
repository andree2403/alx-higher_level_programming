#!/usr/bin/python3
"""shebang"""

import json
"""imported module"""


def to_json_string(my_obj):
    """function that converts to json file"""
    jsonstring = json.dumps(my_obj)
    return jsonstring
