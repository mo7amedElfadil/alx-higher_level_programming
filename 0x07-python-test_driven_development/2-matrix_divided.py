#!/usr/bin/python3
"""
This is the matrix_divided module.

The module supplies one function, matrix_divided().  For example,
    >>> matrix = [[1, 2, 3],[4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

Prototype: def matrix_divided(matrix, div)

Rules:
    matrix must be a list of lists of integers or floats, otherwise:
        raise a TypeError exception with the message:
            "matrix must be a matrix (list of lists) of integers/floats"
    Each row of the matrix must be of the same size, otherwise:
        raise a TypeError exception with the message:
            "Each row of the matrix must have the same size"
    div must be a number (integer or float), otherwise:
        raise a TypeError exception with the message:
            "div must be a number"
    div can’t be equal to 0, otherwise:
        raise a ZeroDivisionError exception with the message:
            "division by zero"
    All elements of the matrix should be divided by div,
        rounded to 2 decimal places
    Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Return the a new matrix made up of the quotients of the matrix
    divided by a number (int / float).


    Parameters:
    - matrix (list): 2D list (n * m) of ints/floats.
    - div (int/float, Optional): number to divide matrix by.

    Returns:
    list:  2D list (n * m) of result of division as floats.

    Example:

    #testing printing return value of matrix_divided when matrix isn't defined
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
        ...
    NameError: name 'matrix' is not defined

    #testing print matrix_divided when matrix is defined
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    #testing when div is a char
    >>> print(matrix_divided(matrix, '3'))
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    #testing when matrix rows aren't the same size
    >>> matrix = [[1, 2, 3], [4, 5]]
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size

    #testing when matrix is none
    >>> print(matrix_divided(None, 3))
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(n, (int, float)) for r in matrix for n in r):

        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
