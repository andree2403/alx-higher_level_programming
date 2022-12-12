#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number) % 10
    if n < 0:
        n = -n
    else:
        n = n
    print(n, end="")
    return (n)
