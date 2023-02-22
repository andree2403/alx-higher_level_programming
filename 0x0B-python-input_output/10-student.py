#!/usr/bin/python3
"""shebang"""


class Student:
    """define a class named student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method for retrieving dict representation"""
        if type(attrs) == list:
            return vars(self.attrs)
        else:
            return vars(self)
