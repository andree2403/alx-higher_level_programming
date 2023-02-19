#!/usr/bin/python3
""" shebang"""


def inherits_from(obj, a_class):
    """ a function that returns true if an object is an instance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
