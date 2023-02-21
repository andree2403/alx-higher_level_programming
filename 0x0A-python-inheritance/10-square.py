#!/usr/bin/python3

"""creation of square class to inherit from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
"""imported module"""

class Square(Rectangle):
    """creatng a class names Square"""
    def __init__(self, size):
        """instalizing the Square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area must be implemented"""
        return self.__size * self.__size

    def __str__(self):
        """string format to print"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size) 
