#!/usr/bin/python3
"""Defining 8-class_to_json module
contains a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    my_dict = {}
    if hasattr(obj, "__dict__"):
        my_dict = obj.__dict__.copy()
    return my_dict
