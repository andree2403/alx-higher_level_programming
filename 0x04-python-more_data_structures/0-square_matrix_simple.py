#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
   squares = [[x ** 2 for x in j] for j in matrix]
   return squares
