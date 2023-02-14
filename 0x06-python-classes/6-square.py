#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute with size"""
        self.__size = size
        self.__position = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""
        return "{}".format(self.__size * self.__size)

    @property
    def size(self):
        """For retrieving the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """For setting the value for the size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square."""
        if self.__size == 0:
            print('')
            return
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end="")
            print()

    @property
    def position(self):
        """for retrieving the value"""
        return self.__position

    @position.setter
    def position(self, value):
        """To set the value"""
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
