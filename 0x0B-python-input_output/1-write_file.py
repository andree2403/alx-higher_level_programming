#!/usr/bin/python3
"""shebang"""


def write_file(filename="", text=""):
    """function that writes and returns no of character"""
    with open(filename, 'w', encoding="utf-8") as g:
        return g.write(text)
