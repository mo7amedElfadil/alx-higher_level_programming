#!/usr/bin/python3
"""Defining 1-my_list module
"""


class MyList(list):
    """Definition of MyList Class
        Inherits from:
            list class
    """
    def __init__(self):
        """Initialize the object
        """
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted
        """
        print(sorted(self))
