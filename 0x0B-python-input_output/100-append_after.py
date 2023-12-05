#!/usr/bin/python3
"""Defining 100-append_after module
contains a function that appends to a text file (UTF8) after
each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """appends to a text file after each line containing a specific string
    mode = a:   Open a file for append.
                If the file already exists, appends text to existing content.
                Create a new file if the file does not exist.
    """
    with open(filename, "r+") as fp:
        lines = fp.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
        fp.seek(0)
        fp.writelines(lines)
