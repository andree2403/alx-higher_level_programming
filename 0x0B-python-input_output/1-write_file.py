#!/usr/bin/python3
"""shebang"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as g:
        return g.write(text)
