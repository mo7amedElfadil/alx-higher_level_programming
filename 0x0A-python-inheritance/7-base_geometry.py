#!/usr/bin/python3
"""Defining 7-base_geometry module
"""


class BaseGeometry():
    """Definition of BaseGeometry Class
    """

    def area(self):
        """ raises Exception with message:
            area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer
            if not then raises TypeError with message:
                <name> must be an integer
            if value is <= 0, raises a ValueError with message:
                <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name:s} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
