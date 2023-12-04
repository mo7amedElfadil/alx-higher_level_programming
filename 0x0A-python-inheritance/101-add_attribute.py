#!/usr/bin/python3
"""Defining 101-add_attribute module
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible:
        If not possible, raises a TypeError exception with message:
            can't add new attribute
        This is done by checking if the object has a __dict__ property or
        object does not have a __slots__ property
    """
    if "__dict__" not in dir(obj) or "__slots__" in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
