#!/usr/bin/python3
"""Defining 4-inherits_from module
"""


def inherits_from(obj, a_class):
    """Tests if object is:
        an instance of the class than inherited (directly or indirectly)
        from, the specified class
    Returns True if it is, False if not
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
