#!/usr/bin/python3
"""Defining 3-to_json_string module
contains a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    """
    import json
    return json.dumps(my_obj)
