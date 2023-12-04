#!/usr/bin/python3
"""Defining 100-my_int module
"""


class MyInt(int):
    """Definition of MyInt Class
        Inherits from int Class
        its == and != operators are inverted
    """
    def __init__(self, value):
        super().__init__()

    def __eq__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.real != other.real

    def __ne__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.real == other.real
