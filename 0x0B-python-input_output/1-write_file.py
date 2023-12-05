#!/usr/bin/python3
"""Defining 1-write_file module
contains a function that write to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """writes to a UTF8 encoded text file and returns number of chars written
    using the with statement to ensure file is closed
    mode = w:   Open a file for writing.
                If the file already exists,
                overwrite its contents.
                Create a new file if the file does not exist.
    """
    with open(filename, "w") as fp:
        char_count = fp.write(text)
    return char_count
