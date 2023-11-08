#!/usr/bin/python3
def square(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    return [list(map(square, x)) for x in matrix]
