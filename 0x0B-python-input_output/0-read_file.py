#!/usr/bin/python3
"""shebang"""


def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        print(read, end='')
