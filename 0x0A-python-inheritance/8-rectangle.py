#!/usr/bin/python3
"""Defines an inherited class-checking function."""


class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """raise exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method def integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(self.__width) != int:
            raise TypeError("{} must be an integer".format(name))
        if self.__width <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(self.__height) != int:
            raise TypeError("{} must be an integer".format(name))
        if self.__height <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """a subclass named rectangle"""
    def __init__(self, width, height):
        """ attributes of a rectangle"""
        self.__width = width
        self.__height = height
