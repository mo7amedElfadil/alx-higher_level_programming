#!/usr/bin/python3
"""Defining 4-from_json_string module
contains a function that returns an object (DS) represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
    """
    import json
    return json.loads(my_str)
