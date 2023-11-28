#!/usr/bin/python3
"""
This is the print_square module.

The module supplies one function, print_square().  For example,
    >>> print_square(4)
    ####
    ####
    ####
    ####

Prototype: def print_square(size):

Rules:
    size is the size length of the square
    size must be an integer, otherwise:
        raise a TypeError exception with the message:
            size must be an integer
    if size is less than 0,
        raise a ValueError exception with the message:
            size must be >= 0
if size is a float and is less than 0,
    raise a TypeError exception with the message:
        size must be an integer

"""


def print_square(size):
    """definition of print_square function
    Parameters:
        size (int): size of square.
    Returns:
        Nothing.

    Example:
    #testing execution with correct arguments
    >>> print_square(3)
    ###
    ###
    ###

    #testing with size 0
    >>> print_square(0)
    <BLANKLINE>

    #testing with negative size
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

    #testing when size is a float
    >>> print_square(1.0)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    #testing when size is a str (none int)
    >>> print_square('3')
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    #testing with no args
    >>> print_square()
    Traceback (most recent call last):
        ...
    TypeError: print_square() missing 1 required positional argument: 'size'

    #testing with more than 1 arg
    >>> print_square(3, 56)
    Traceback (most recent call last):
        ...
    TypeError: print_square() takes 1 positional argument but 2 were given

    #testing when size is None
    >>> print_square(None)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if (size == 0):
        print()
        return
    for _ in range(size):
        print("#" * size)
