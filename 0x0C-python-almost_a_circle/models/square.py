#!/usr/bin/python3
"""Defines a Base class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a new class named square"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the representation of the answer"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        """returns the width"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
