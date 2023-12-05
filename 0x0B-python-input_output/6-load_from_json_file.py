#!/usr/bin/python3
"""Defining 6-load_from_json_file module
contains a function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """creates and returns an Object from a “JSON file”
    """
    import json
    with open(filename, "r") as fp:
        return json.load(fp)
