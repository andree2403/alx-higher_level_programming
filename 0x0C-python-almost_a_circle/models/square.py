#!/usr/bin/python3
"""Defines a Base class"""
from models.Rectangle import Rectangle


class Square(Rectangle):
    """a new class named square"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of attributes"""
        super().__init__(size, size, x, y, id)
