#!/usr/bin/python3
"""Defining 100-my_int module
"""


class MyInt(int):
    """Definition of MyInt Class
        Inherits from int Class
        its == and != operators are inverted
    """
    def __init__(self, value):
        """instantiate instance of the class"""
        super().__init__()

    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """equality operator, returns True when theyre not equal"""
        if not isinstance(other, int):
            return NotImplemented
        return self.real != other.real

    def __ne__(self, other):
        """inequality operator, returns True when theyre equal"""
        if not isinstance(other, int):
            return NotImplemented
        return self.real == other.real
