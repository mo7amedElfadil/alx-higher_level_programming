#!/usr/bin/python3
"""Defining 0-lookup module
"""


def lookup(obj):
    """Definition of lookup function
        Args:
            obj: object
        Description:
            returns the list of available attributes and methods of an object
    """
    return dir(obj)
