#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if a == 8 and b == 9:
            print("{}{}\n".format(a, b), end="")
        else:
            print("{}{}, ".format(a, b), end="")
