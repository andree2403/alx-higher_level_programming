#!/usr/bin/python3
def element_at(my_list, idx):
    for i in idx:
        if i < 0:
            return None
        elif i > idx:
            return None
        else:
            print("Element at index {:d} is {}".format(i, my_list[i]))
