#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    if n < 0:
        n = n * -1
    else:
        return(n)
    print("{}".format(n), end="")
