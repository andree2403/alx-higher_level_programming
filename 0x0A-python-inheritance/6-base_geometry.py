#!/usr/bin/python3
"""Defines an inherited class-checking function."""


class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """raise exception with a message"""
        raise Exception("area() is not implemented")
