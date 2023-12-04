#!/usr/bin/python3
"""Defining 3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """Tests if object is:
        an instance of the class specified or,
        an instance of a class that inherited from, the specified class
    Returns True if it is, False if not
    """
    return isinstance(obj, a_class)
