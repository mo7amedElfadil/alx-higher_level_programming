#!/usr/bin/python3
"""
This is the say_my_name module.

The module supplies one function, say_my_name().  For example,
    >>> say_my_name("John", "Smith")
    My name is John Smith

Prototype:def say_my_name(first_name, last_name=""):

Rules:
    first_name and last_name must be strings otherwise:
        raise a TypeError exception with the message:
            "first_name must be a string or last_name must be a string"

"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Parameters:
    - first_name (string): First name to be printed.
    - last_name (string, Optional): Last name to be printed
                empty string by default.

    Returns:
        Nothing.
    Example:
    #testing execution with correct arguments
    >>> say_my_name("John", "Smith")
    My name is John Smith

    #testing when first name is an int (none str)
    >>> say_my_name(12, "Smith")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

    #testing when last name is an int (none str)
    >>> say_my_name("John", 12)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

    #testing with one argument is passed
    >>> say_my_name("John")
    My name is John \n

    #testing when first name is none
    >>> say_my_name(None, "Bob")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
