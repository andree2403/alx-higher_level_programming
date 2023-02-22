#!/usr/bin/python3
"""shebang"""

import json
""" imported module"""


def class_to_json(obj):
    """a function that returns a simple dictionary"""
    return vars(obj)
