#!/usr/bin/python3
def islower(str):
    for i in str:
        i = ord(i)
        if i >= 65 and i < 91:
            print({}.format(str), end="")
        else:
            print({}.format(str - 32), end="")

