#!/usr/bin/python3
"""Defining 2-append_write module
contains a function that appends to a text file (UTF8)
"""


def append_write(filename="", text=""):
    """appends to a UTF8 encoded text file and returns number of chars written
    using the with statement to ensure file is closed
    mode = a:   Open a file for append.
                If the file already exists, appends text to existing content.
                Create a new file if the file does not exist.
    """
    with open(filename, "a") as fp:
        char_count = fp.write(text)
    return char_count
