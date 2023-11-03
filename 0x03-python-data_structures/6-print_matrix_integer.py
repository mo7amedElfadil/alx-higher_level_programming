#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, col in enumerate(row):
            print(col, end=(" ", "\n")[i == len(row) - 1])
