#!/usr/bin/python3
"""Defines a Base class"""
from models.base import Base


class Rectangle(Base):
    """create a class named rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the value of width"""
        self.__width = width


    @property
    def height(self):
        """gets the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the value of height"""
        self.__height = height

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the value of width"""
        self.__x = x

    @property
    def y(self):
        """gets the value of width"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the value of width"""
        self.__y = y
