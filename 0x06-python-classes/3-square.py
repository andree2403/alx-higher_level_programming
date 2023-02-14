#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Private instance attribute with size"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""
        return "{}".format(self.__size * self.__size)
