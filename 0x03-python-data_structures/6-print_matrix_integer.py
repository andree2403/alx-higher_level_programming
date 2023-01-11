#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for j in range(len(matrix[x])):
            endspace = " "
            if j == len(matrix[x]) - 1:
                endspace = ""
            print("{:d}".format(matrix[x][j]), end=endspace)
        print()
