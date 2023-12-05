#!/usr/bin/python3
"""Defining 0-read_file module
contains a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """reads a UTF8 encoded text file and prints it to stdout
    using the with statement to ensure file is closed
    mode = r: Open a file for reading. This is the default mode.
    """
    with open(filename, "r", encoding="utf-8") as fp:
        file = fp.read()
        print(file, end="")
