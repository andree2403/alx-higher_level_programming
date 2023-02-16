#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """create a class named Rectangle"""

    # Public
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """attributes of the class"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """should print the rectangle with the character"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            if i == self.__height - 1:
                result += (str(self.print_symbol) * self.__width)
            else:
                result += ((str(self.print_symbol) * self.__width) + '\n')
        return result

    def __repr__(self):
        """ return a string representation of the rectangle"""
        w = str(self.__width)
        h = str(self.__height)
        result = "Rectangle(" + w + ", " + h + ")"
        return result

    def __del__(self):
        """print a message when you delete an instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns which area is bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        height = size
        width = size
        return cls(height, width)
