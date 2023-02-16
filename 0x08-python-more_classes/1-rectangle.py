#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """create a class named Rectangle"""
    def __init__(self, width=0, height=0):
        """attributes of the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """function that retrieves width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """function that sets the value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """function that returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function that sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
