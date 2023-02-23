#!/usr/bin/python3
"""shebang"""


def pascal_triangle(n):
    lists = []
    if n <= 0:
        return lists
    if n > 0:
        i = 1
        while i <= n:
            x = list(lambda a, b : (a + b) ** i)
            print(x(i, i))
            i += 1
