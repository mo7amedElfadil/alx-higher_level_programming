#!/usr/bin/python3
"""Defining 3-to_json_string module
contains a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    import json
    """returns the JSON representation of an object (string)
    """

    return str(json.dumps(my_obj))
