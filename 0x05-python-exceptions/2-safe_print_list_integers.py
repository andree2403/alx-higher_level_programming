#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    i = x - 1
    for j in range(i + 1):
        try:
            if type(my_list[j]) != int:
                continue
            else:
                print("{:d}".format(my_list[j]), end='')
            n += 1
        except(ValueError, TypeError):
            continue
    print()
    return n
