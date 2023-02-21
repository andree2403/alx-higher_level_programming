#!/usr/bin/python3
"""Defines an inherited class-checking function."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""rectangle module"""


class Rectangle(BaseGeometry):
    """a subclass named rectangle"""
    def __init__(self, width, height):
        """ attributes of a rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """area must be implemented"""
        return self.__width * self.__height

    def __str__(self):
        """string format to print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
