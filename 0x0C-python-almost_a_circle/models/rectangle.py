#!/usr/bin/python3
"""Defines a Base class"""
from models.base import Base


class Rectangle(Base):
    """create a class named rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the value of width"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays with #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns the representation of the answer"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """update an assign argument"""
        if len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.__width = v
                if k == 'height':
                    self.__height = v
                if k == 'x':
                    self.__x = v
                if k == 'y':
                    self.__y = v
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
