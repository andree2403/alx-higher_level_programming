#!/usr/bin/python3
"""shebang"""


def append_write(filename="", text=""):
    """function that appends a text to a file"""
    with open(filename, 'a', encoding="utf-8") as g:
        return g.write(text)
