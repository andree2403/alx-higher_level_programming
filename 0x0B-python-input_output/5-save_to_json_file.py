#!/usr/bin/python3
"""shebang"""

import json
""" imported module"""


def save_to_json_file(my_obj, filename):
    """function to save json file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dumps(my_obj, f)
