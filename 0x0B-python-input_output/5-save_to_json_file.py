#!/usr/bin/python3
"""Defining 5-save_to_json_file module
contains a function that writes an Object to a text file,
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    import json
    """writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w") as fp:
        json.dump(my_obj, fp)
