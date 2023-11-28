#!/usr/bin/python3
"""
This is the add_integer module.

The module supplies one function, add_integer().  For example,

    >>> add_integer(5, 7)
    12

"""


def add_integer(a, b=98):
    """
    Return the sum of 2 integers.

    Parameters:
    - a (int/float): First integer to add.
    - b (int/float, Optional): Second integer to add.

    Returns:
    int: Sum of 2 given integers, a + b

    Example:
    >>> add_integer(4, 5)
    9
    >>> add_integer(-3, 10)
    7
    >>> add_integer(4.5, 7)
    11
    >>> add_integer('3', 5)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(4, "integer")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer([4], 5)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer


    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
