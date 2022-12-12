#!/usr/bin/python3
def islower(str):
    for i in str:
        i = ord(i)
        if i >= 65 and i < 91:
            print({}.format(i), end="")
        else:
            print({}.format(i - 32), end="")

