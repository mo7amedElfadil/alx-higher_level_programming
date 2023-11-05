#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
        for i, col in enumerate(row):
            print("{:d}".format(col), end=(" ", "\n")[i == len(row) - 1])
