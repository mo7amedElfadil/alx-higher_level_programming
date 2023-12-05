#!/usr/bin/python3
"""Defining 12-pascal_triangle module
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing pascal's triangle of n
    eg:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    pas = []
    for i in range(1, n + 1):
        pas.append([])
        v = 1
        for j in range(1, i + 1):
            pas[i - 1].append(v)
            v = v * (i - j) // j
    return pas
