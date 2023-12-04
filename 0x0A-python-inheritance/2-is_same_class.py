#!/usr/bin/python3
"""Defining 2-is_same_class module
"""


def is_same_class(obj, a_class):
    """Tests if object is exactly an instance of specified class
    Returns True if it is, False if not
    """
    return type(obj) is a_class
