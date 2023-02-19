#!/usr/bin/python3
"""shebang"""

class MyList(list):
    """a class mylist that inherits from a class list"""
    def print_sorted(self):
        """a function that returns a sorted list"""
        print(sorted(self))
