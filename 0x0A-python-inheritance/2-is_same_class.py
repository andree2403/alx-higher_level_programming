#!/usr/bin/python3
""" shebang"""


def is_same_class(obj, a_class):
    """ a function that returns true if an object is an instance"""
    if type(obj) == a_class:
        return True
    else:
        return False
